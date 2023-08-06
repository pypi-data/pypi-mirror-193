# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0
import ast
import contextlib
import shutil
import sys
from io import StringIO
from pathlib import Path


def set_paths_to_use_lib():
    script = Path(__file__).resolve()
    project_dir = script.parent.parent
    lib_dir = project_dir / "lib"
    for wheel in lib_dir.glob("*.whl"):
        sys.path.insert(0, str(wheel))
    sys.path.insert(0, str(project_dir))


set_paths_to_use_lib()

from coveriteam import coveriteam


@contextlib.contextmanager
def enabled_download():
    try:
        coveriteam.util.set_cache_update(True)
        cache_dir = Path(__file__).resolve().parent / "cache"
        coveriteam.util.set_cache_directories(cache_dir)
        cache_dir.mkdir(exist_ok=True)
        yield cache_dir
    finally:
        coveriteam.util.set_cache_update(False)
        coveriteam.util.set_cache_directories(None)
        shutil.rmtree(cache_dir)


# from https://stackoverflow.com/a/17981937/3012884
@contextlib.contextmanager
def capture_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def extract_verdict_from_output(func, *args, **kwargs) -> str:
    with capture_output() as (out, err):
        func(*args, **kwargs)
    last_line = out.getvalue().splitlines()[-1]
    result_dict = ast.literal_eval(last_line)
    assert type(result_dict) is dict
    return result_dict["verdict"]
