# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2021 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import importlib
import pathlib
import sys
from typing import NamedTuple, Sequence
from test_util import capture_output

import pytest

import coveriteam.util as util


class Run(NamedTuple):
    cmdline: str
    output: Sequence[str]


import benchexec

benchexec_toolinfo = importlib.import_module(
    "benchexec.tools.coveriteam-verifier-validator"
)


from coveriteam.coveriteam import CoVeriTeam

DIR_EXAMPLES = pathlib.Path("examples")
DIR_TEST_DATA = DIR_EXAMPLES / "test-data"
DIR_PROGRAMS = DIR_TEST_DATA / "c"
PATH_UNREACH_PROP = DIR_TEST_DATA / "properties" / "unreach-call.prp"
DIR_CCEGAR = DIR_EXAMPLES / "Component-based_CEGAR"


def get_core_compositions():
    """Return C-CEGAR compositions that suffice to test the basic functionality of C-CEGAR.

    These compositions allow to check that C-CEGAR in CoVeriTeam:

    * can prove a program safe
    * find violations

    They should be able to solve the tasks "jain_1-1.c" and "rangesum.i",
    but need multiple iterations for it.
    """
    compositions = [
        DIR_CCEGAR / c
        for c in (
            "cCegar-predmap_cex-cpachecker_ref-cpachecker.cvt",
            "cCegar-invariantWitness_cex-cpachecker_ref-cpachecker.cvt",
        )
    ]
    assert all(c.exists() for c in compositions)
    return compositions


def get_all_compositions():
    """Return all C-CEGAR compositions shipped with CoVeriTeam."""
    return DIR_CCEGAR.glob("*.cvt")


def setup_module():
    util.set_cache_directories()


def _run_and_check_verdict(inputs, expected_verdict):
    with capture_output() as (out, err):
        CoVeriTeam().start(inputs)
    run = Run(cmdline=" ".join(inputs), output=out.getvalue().splitlines())
    verdict = benchexec_toolinfo.Tool().determine_result(run)
    assert verdict == expected_verdict, (
        f"Actual verdict '{verdict}' != '{expected_verdict}' (expected)\nRecorded CoVeriTeam output:\n"
        + "\n".join(run.output)
    )


def test_all_cCegar_proves_in_first_iteration_sanfoundry_43_ground():
    compositions = get_all_compositions()
    _check_set_cCegar_proves_in_first_iteration_sanfoundry_43_ground(compositions)


def test_core_cCegar_proves_in_first_iteration_sanfoundry_43_ground():
    compositions = get_core_compositions()
    _check_set_cCegar_proves_in_first_iteration_sanfoundry_43_ground(compositions)


def _check_set_cCegar_proves_in_first_iteration_sanfoundry_43_ground(compositions):
    for composition in compositions:
        _check_cCegar_proves(composition, DIR_PROGRAMS / "sanfoundry_43_ground.i")


def _check_cCegar_proves(composition, program):
    inputs = [str(composition)]
    inputs += ["--input", f"program_path={program}"]
    inputs += ["--input", f"specification_path={PATH_UNREACH_PROP}"]
    _run_and_check_verdict(inputs, expected_verdict=benchexec.result.RESULT_TRUE_PROP)


def test_all_cCegar_violation_in_first_iteration_error():
    compositions = get_all_compositions()
    _check_set_cCegar_violation_in_first_iteration_error(compositions)


def test_core_cCegar_violation_in_first_iteration_error():
    compositions = get_core_compositions()
    _check_set_cCegar_violation_in_first_iteration_error(compositions)


def _check_set_cCegar_violation_in_first_iteration_error(compositions):
    for composition in compositions:
        yield _check_cCegar_violation, composition, DIR_PROGRAMS / "error.i"


def _check_cCegar_violation(composition, program):
    if "symbiotic" in composition.name.lower() and sys.version_info[1] != 8:
        # symbiotic only runs on python 3.8
        raise pytest.skip()
    inputs = [str(composition)]
    inputs += ["--input", f"program_path={program}"]
    inputs += ["--input", f"specification_path={PATH_UNREACH_PROP}"]
    _run_and_check_verdict(inputs, expected_verdict=benchexec.result.RESULT_FALSE_REACH)


def test_core_cCegar_prove_multiple_cycles():
    compositions = get_core_compositions()
    for composition in compositions:
        _check_cCegar_proves(composition, DIR_PROGRAMS / "jain_1-1.c")


def test_core_cCegar_violation_multiple_cycles():
    compositions = get_core_compositions()
    for composition in compositions:
        _check_cCegar_violation(composition, DIR_PROGRAMS / "rangesum.i")
