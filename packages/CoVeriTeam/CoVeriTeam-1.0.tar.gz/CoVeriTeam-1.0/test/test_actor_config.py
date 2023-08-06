# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2021 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import os
from io import BytesIO
from pathlib import Path
from typing import List

from pytest import raises  # noqa PT013
import unittest.mock as mock

from test_util import enabled_download
import requests
from coveriteam import coveriteam
from coveriteam.language import CoVeriLangException
from coveriteam.language.actorconfig import (
    dict_merge,
    ActorConfig,
    ActorDefinitionLoader,
)

# If this import id missing, then the call `benchexec.util.<func>` will
# fail. This may be caused by coveriteams import magic.
import benchexec.util  # noqa F401
from coveriteam.util import unzip  # noqa F401

all_yaml_files: List[Path]

files_to_skip = {
    "cpachecker-BASE.yml",
    "condtest.yml",
    "cst-transform.yml",
    "verifier_resource.yml",
    "verifier+validator-portfolio.yml",
}


def setup_module():
    global all_yaml_files
    coveriteam.util.set_cache_directories()
    coveriteam.util.set_cache_update(False)
    os.chdir(Path(os.path.realpath(__file__)).parent.parent)
    actor_path = Path(os.getcwd()) / "actors"
    all_yaml_files = [
        (actor_path / file_string).resolve()
        for file_string in os.listdir(str(actor_path))
        if (actor_path / file_string).resolve().suffix == ".yml"
    ]


def test_dict_merge():
    d1 = {"a": "b", "b": "b", "c": "d"}
    d2 = {"c": "e"}
    d3 = {"dict": d2}
    d4 = d2.copy()
    d4["dict"] = "no_dict"

    assert {"a": "b", "b": "b", "c": "e"} == dict_merge(d1, d2)
    assert {"c": "e", "dict": d2} == dict_merge(d2, d3)

    # Should throw an exception with the current solution
    with raises(CoVeriLangException):
        dict_merge(d4, d2)


def yaml_correct_loaded(actor_config: ActorConfig, version: str):
    assert actor_config.path is not None
    assert str(version) == str(actor_config.version)
    assert actor_config.tool_dir is not None
    assert len(actor_config.actor_name) > 0

    try:
        actor_config.archive_location
    except AttributeError:
        # If the version uses a DOI as archive location the archive_location does not get created
        return

    # This is not part of the coveriteam code; this should be moved
    # to a separate pipeline stage.
    # is_valid_download_url(actor_config.archive_location) noqa E800

    tool_dir_name = Path(actor_config.get_tool_installation_dir()).name
    archive_name = actor_config.archive_name.replace(".zip", "")
    assert tool_dir_name.startswith(
        archive_name
    ), "Tool dir of %s has wrong name: %s" % (actor_config.actor_name, tool_dir_name)
    assert version in actor_config.actor_name, (
        "Actor name of %s does not include the version" % actor_config.actor_name
    )


def is_valid_download_url(url: str):
    """Checks, if the given url is valid by retrieving only the headers"""
    answer: requests.Response = requests.head(url=url)
    assert 200 == answer.status_code, "Error %s while checking %s" % (
        answer.status_code,
        url,
    )


def test_all_yaml_file_integrity():
    class TestActorConfig(ActorConfig):
        """Prints the file name of this actor for the generated tests"""

        def __repr__(self) -> str:
            return str(self.path.name)

    global all_yaml_files
    ActorDefinitionLoader.add_constructor("!include", ActorDefinitionLoader.include)
    for file in all_yaml_files:
        if file.name in files_to_skip:
            continue
        config = ActorDefinitionLoader.load_config(file)
        if "archives" not in config or not config["archives"]:
            continue
        for archive in config["archives"]:
            version = archive["version"]
            actor_config = TestActorConfig(file, version)
            yaml_correct_loaded(actor_config, version)


@mock.patch("requests.get")
@mock.patch("requests.head")
@mock.patch("coveriteam.language.actorconfig.unzip")
@mock.patch(
    "coveriteam.language.actorconfig.ActorConfig._ActorConfig__resolve_tool_info_module"
)
def test_download_if_needed(
    mock_resolve,
    mock_unzip: mock.MagicMock,
    mock_head: mock.MagicMock,
    mock_get: mock.MagicMock,
):
    response_head_mock = mock.MagicMock(spec=requests.Response)
    type(response_head_mock).headers = mock.PropertyMock(
        return_value={"etag": "deadbeef"}
    )
    type(response_head_mock).status_code = mock.PropertyMock(return_value=200)

    response_mock = mock.MagicMock(spec=requests.Response)
    type(response_mock).headers = mock.PropertyMock(
        return_value={"content-length": 4096, "etag": "deadbeef"},
    )
    type(response_mock).status_code = mock.PropertyMock(return_value=200)
    response_mock.iter_content.return_value = BytesIO(b"\x00" * 4096)

    mock_get.return_value = response_mock
    mock_head.return_value = response_head_mock

    with enabled_download():
        # Check download of zip
        print("Downloading actor 1st time from location")
        cpa_seq = ActorConfig("actors/cpa-seq.yml", "svcomp22")  # Download 1st time
        archive_download_path = (
            coveriteam.util.get_ARCHIVE_DOWNLOAD_PATH() / cpa_seq.archive_name
        )
        print("Downloading actor 2nd time from location")
        assert not coveriteam.util.download_if_needed(  # Download 2nd time
            cpa_seq.archive_location, archive_download_path
        ), "Downloaded actor a second time, but it was not needed"

        print(mock_unzip.call_args())


# TODO: This test downloads a large archive from Zenodo and is thus slow
# Mock the Zenodo response to make this test fast and independent
def test_download_if_needed_with_doi():
    with enabled_download():
        # Check download of DOI
        print("Downloading actor 1st time with DOI")
        cpa_seq = ActorConfig("actors/cpa-seq.yml", "2.1")  # Download 1st time
        archive_download_path = (
            coveriteam.util.get_ARCHIVE_DOWNLOAD_PATH() / cpa_seq.archive_name
        )
        print("Downloading actor 2nd time with DOI")
        assert not coveriteam.util.download_if_needed(  # Download 2nd time
            cpa_seq.archive_location, archive_download_path
        ), "Downloaded actor DOI a second time, but it was not needed"
