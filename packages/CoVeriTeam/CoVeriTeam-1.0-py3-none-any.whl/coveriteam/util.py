# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import os
import re
import shutil
import sys
import urllib.request
from pathlib import Path
from typing import Dict, Type, List, TYPE_CHECKING, Callable
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo

import requests
from tqdm import tqdm

from coveriteam.language import CoVeriLangException

if TYPE_CHECKING:
    from coveriteam.language.artifact import Artifact

LOG_DIR = Path.cwd() / "cvt-output"
TOOL_OUTPUT_FILE = "output.txt"
INPUT_FILE_DIR = f'{Path(__file__).parent.resolve() / "artifactlibrary/"}/'
PORTFOLIO_USE_MPI = False
CURRENTLY_IN_MPI = False
DOWNLOAD_CHUNK_SIZE = 4096

CVT_DEBUG_LEVEL = 15


def set_cache_directories(d=None):
    global INSTALL_DIR, ARCHIVE_DOWNLOAD_PATH, TOOL_INFO_DOWNLOAD_PATH, CACHE_DIR_PATH
    if d:
        cache_dir = d
    elif os.getenv("XDG_CACHE_HOME"):
        cache_dir = Path(os.getenv("XDG_CACHE_HOME")) / "coveriteam"
    else:
        cache_dir = Path.home() / ".cache" / "coveriteam"
    CACHE_DIR_PATH = str(cache_dir.resolve())
    INSTALL_DIR = cache_dir / "tools"
    ARCHIVE_DOWNLOAD_PATH = cache_dir / "archives"
    TOOL_INFO_DOWNLOAD_PATH = cache_dir / "toolinfocache"
    sys.path.append(str(TOOL_INFO_DOWNLOAD_PATH))
    create_cache_directories()


def set_cache_update(flag):
    global UPDATE_CACHE
    UPDATE_CACHE = flag


def set_use_mpi_flag(flag):
    global PORTFOLIO_USE_MPI
    if flag:
        PORTFOLIO_USE_MPI = True
    else:
        PORTFOLIO_USE_MPI = False


def create_cache_directories():
    # Create directories and set path.
    if not ARCHIVE_DOWNLOAD_PATH.is_dir():
        ARCHIVE_DOWNLOAD_PATH.mkdir(parents=True)
    if not TOOL_INFO_DOWNLOAD_PATH.is_dir():
        TOOL_INFO_DOWNLOAD_PATH.mkdir(parents=True)

    if not INSTALL_DIR.is_dir():
        INSTALL_DIR.mkdir(parents=True)


def get_INSTALL_DIR():
    return INSTALL_DIR


def get_ARCHIVE_DOWNLOAD_PATH():
    return ARCHIVE_DOWNLOAD_PATH


def get_TOOL_INFO_DOWNLOAD_PATH():
    return TOOL_INFO_DOWNLOAD_PATH


def get_CACHE_DIR_PATH():
    return CACHE_DIR_PATH


def is_url(path_or_url):
    return "://" in path_or_url or path_or_url.startswith("file:")


def make_url(path_or_url):
    """Make a URL from a string which is either a URL or a local path,
    by adding "file:" if necessary.
    """
    if not is_url(path_or_url):
        return "file:" + urllib.request.pathname2url(path_or_url)
    return path_or_url


def download_if_needed(location, target):
    url = make_url(location)
    headers = {"User-Agent": "Mozilla"}
    etag_path = Path(str(target) + ".etag")
    if etag_path.is_file() and target.is_file():
        saved_etag = etag_path.open("r").read()
        response = requests.head(url, allow_redirects=True, headers=headers)
        try:
            if response.headers["etag"] == saved_etag:
                # No need to download in this case
                return False
        except KeyError:
            # Temporary: printing messages to figure out what is the problem when downloading from Zenodo
            # It seems that sometimes we are not able to download Zenodo based archives
            print("------------------DEBUG----------------------")
            print("ETAG not present in the response")
            print(response.headers)

    try:
        response = requests.get(url, allow_redirects=True, headers=headers, stream=True)
        if response.status_code != 200:
            msg = (
                "Couldn't download tool archive from: %s. Server returned the code: %s"
                % (str(url), response.status_code)
            )
            raise CoVeriLangException(msg)
        with target.open("wb") as out_file:
            content_length = response.headers.get("content-length")
            content_length = int(content_length) if content_length else 0
            for data in tqdm(
                response.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE),
                total=int(content_length / DOWNLOAD_CHUNK_SIZE),
                unit_scale=int(DOWNLOAD_CHUNK_SIZE / 1000),
                unit="KB",
            ):
                out_file.write(data)
        # write the eta tag
        try:
            etag = response.headers["etag"]
            with Path(str(target) + ".etag").open("w") as f:
                f.write(etag)
        except KeyError:
            pass  # no etag to cache
        return True
    except requests.ConnectionError:
        print("No network access. Running in offline mode.")
        return False


def create_archive(dirname, archive_path):
    with ZipFile(archive_path, "w", ZIP_DEFLATED) as zipf:
        for root, _dirs, files in os.walk(dirname):
            for f in files:
                filepath = os.path.join(root, f)
                zipf.write(filepath, os.path.relpath(filepath, dirname))


def unzip(archive, target_dir):
    if target_dir.is_dir():
        shutil.rmtree(target_dir)

    with ZipFile(archive, "r") as zipfile:
        top_folder = INSTALL_DIR / zipfile.filelist[0].filename.split("/")[0]
        # Not to use extract all as it does not preserves the permission for executable files.
        # See: https://bugs.python.org/issue15795
        # See https://stackoverflow.com/questions/39296101/python-zipfile-removes-execute-permissions-from-binaries
        for member in zipfile.namelist():
            if not isinstance(member, ZipInfo):
                member = zipfile.getinfo(member)
            extracted_file = zipfile.extract(member, INSTALL_DIR)
            # This takes first two bytes from four bytes.
            attr = member.external_attr >> 16
            if attr != 0:
                os.chmod(extracted_file, attr)
        top_folder.rename(target_dir)


def filter_dict(d, keys_to_keep):
    """Filters the first dict by the keys given as second parameter."""
    return {k: d[k] for k in d if k in keys_to_keep}


def complete_outputs(
    provided_outputs: Dict[str, "Artifact"],
    expected_outputs: Dict[str, Type["Artifact"]],
) -> Dict[str, "Artifact"]:
    """Returns a dictionary with all expected outputs. Outputs not provided by provided_outputs are initialized with the neutral version of each artifact type."""
    return {
        k: provided_outputs[k] if k in provided_outputs else expected_outputs[k]()
        for k in expected_outputs
    }


def str_dict(d):
    return {k: str(d[k]) for k in d.keys()}


def artifact_name_clash(
    required_dict: Dict[str, Type["Artifact"]],
    provided_dict: Dict[str, Type["Artifact"]],
    allow_both_directions: bool = False,
) -> bool:
    """This function checks for a name clash in the provided dictionaries

    A name clash exists if a key of the required_dict is also in the provided dict and its value in the required_dict is NOT a subtype of the provided value.
    For example:
        if key in required_dict and in provided_dict:
            required_dict[key] => provided_dict[key]

    If allow_both_directions is True the following applies:
        if key in required_dict and in provided_dict:
            required_dict[key] => provided_dict[key]
            OR
            required_dict[key] <= provided_dict[key]

    Args:
        required_dict: Most of the time the input of an actor
        provided_dict: Most of the time provided inputs to a composition
        allow_both_directions: If subclassing should be allowed in both directions

    Returns:
        True, if a name clash exists between the two dictionaries
    """
    for k in required_dict.keys():
        if k in provided_dict.keys() and not issubclass(
            provided_dict[k], required_dict[k]
        ):
            if not allow_both_directions:
                return True
            if not issubclass(required_dict[k], provided_dict[k]):
                return True

    return False


def get_type_per_key_dict_list(
    type_dicts: List[Dict], selector: Callable[[Type, Type], Type]
) -> Dict[str, Type]:
    """Like util.get_type_per_key(), but accepts a list of dictionaries instead of only two"""
    if len(type_dicts) == 1:
        return type_dicts[0]
    if len(type_dicts) == 2:
        return get_type_per_key(type_dicts[0], type_dicts[1], selector)

    return get_type_per_key(
        type_dicts[0],
        get_type_per_key_dict_list(type_dicts[1:], selector),
        selector,
    )


def get_type_per_key(
    type_dict_one: Dict[str, Type],
    type_dict_two: Dict[str, Type],
    selector: Callable[[Type, Type], Type],
) -> Dict[str, Type]:
    """Returns a dictionary of the types selected by the selector.

    The returned dictionary will contain all keys from both dictionaries.
    If a key exists in both dictionaries, its value is defined by the selector.
    If not, the value stays the same

    Args:
        type_dict_one: A dictionary with types as values
        type_dict_two: A dictionary with types as values
        selector: A callable (for example a function), which accepts two types as input and returns a type

    Returns:
        A dictionary with every key from both input dictionaries
    """
    return_dict = {}

    for name, artifact_type in type_dict_one.items():
        if name not in type_dict_two.keys():
            return_dict[name] = type_dict_one[name]
        else:
            return_dict[name] = selector(artifact_type, type_dict_two[name])

    # Add missing values from type_dict_two
    return_dict.update({k: v for k, v in type_dict_two.items() if k not in return_dict})
    return return_dict


def rename_dict(d, renaming_map):
    return {(renaming_map.get(k, None) or k): d[k] for k in d.keys()}


def collect_variables(exp):
    regex_isinstance = r"(?<=isinstance\()\S+(?=,)"
    regex_in = r"\w+(?= in \[)"
    regex = regex_isinstance + "|" + regex_in
    names = re.findall(regex, exp)

    return names


def get_additional_paths_for_container_config():
    base_dir = Path(__file__).parent.parent.resolve()
    paths = [str(base_dir / "lib"), str(base_dir / "coveriteam" / "toolconfigs")]
    return paths


def specific_type_selector(type1: Type, type2: Type) -> Type:
    """Returns the type, which is a subclass of the other

    For example for
        type1 = Artifact and
        type2 = Verdict
    the returned type is Verdict

    Args:
        type1: A type which should be comparable to type2
        type2: A type which should be comparable to type1

    Returns:
        The more generic type

    Raises:
        ValueError: If one type is not a subtype of the other
    """
    if issubclass(type1, type2):
        return type1

    if issubclass(type2, type1):
        return type2

    raise ValueError("Not possible to compare %s and %s" % (type1, type2))


def generic_type_selector(type1: Type, type2: Type) -> Type:
    """Returns the type, which is a super class of the other

    For example for
        type1 = Artifact and
        type2 = Verdict
    the returned type is Artifact

    Args:
        type1: A type which should be comparable to type2
        type2: A type which should be comparable to type1

    Returns:
        The more generic type

    Raises:
        ValueError: If one type is not a subtype of the other
    """
    if issubclass(type1, type2):
        return type2

    if issubclass(type2, type1):
        return type1

    raise ValueError("Not possible to compare %s and %s" % (type1, type2))
