# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import os

import pytest

import coveriteam.util as util
from coveriteam.coveriteam import CoVeriTeam
from test_util import extract_verdict_from_output


def setup_module():
    os.chdir("examples")
    util.set_cache_directories()


def teardown_module():
    os.chdir("..")


def test_tutorial_verifier():
    inputs = ["verifier-C.cvt"]
    inputs += ["--input", "verifier_path=../actors/cpa-seq.yml"]
    inputs += ["--input", "program_path=test-data/c/Problem02_label16.c"]
    inputs += ["--input", "specification_path=test-data/properties/unreach-call.prp"]
    inputs += ["--input", "verifier_version=default"]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


def test_tutorial_validating_verifier():
    inputs = ["validating-verifier.cvt"]
    inputs += ["--input", "program_path=test-data/c/Problem02_label16.c"]
    inputs += ["--input", "specification_path=test-data/properties/unreach-call.prp"]
    inputs += [
        "--input",
        "validator_path=../actors/cpa-validate-violation-witnesses.yml",
    ]
    inputs += ["--input", "validator_version=default"]
    inputs += ["--input", "verifier_path=../actors/uautomizer.yml"]
    inputs += ["--input", "verifier_version=default"]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


def test_execution_based_validation():
    inputs = ["execution-based-validation.cvt"]
    inputs += ["--input", "program_path=test-data/c/Problem01_label15.c"]
    inputs += ["--input", "specification_path=test-data/properties/unreach-call.prp"]
    inputs += [
        "--input",
        "witness_path=test-data/witnesses/Problem01_label15_reach_safety.graphml",
    ]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


@pytest.mark.skip()
def test_execution_based_validation_witness_instrument():
    inputs = ["exe-validator-witness-instrument.cvt"]
    inputs += ["--input", "program_path=test-data/c/gcnr2008.i"]
    inputs += ["--input", "specification_path=test-data/properties/unreach-call.prp"]
    inputs += [
        "--input",
        "witness_path=test-data/witnesses/gcnr2008_violation_witness.graphml",
    ]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


def test_cmc_reducer():
    inputs = ["reducer-based-conditional-model-checker.cvt"]
    inputs += ["--input", "program_path=test-data/c/slicingReducer-example.c"]
    inputs += ["--input", "specification_path=test-data/properties/unreach-call.prp"]
    inputs += ["--input", "cond_path=test-data/c/slicingCondition.txt"]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


def test_condtest():
    inputs = ["CondTest/condtest.cvt"]
    inputs += ["--gen-code"]
    inputs += ["--input", "program_path=test-data/c/test.c"]
    inputs += [
        "--input",
        "specification_path=test-data/properties/coverage-branches.prp",
    ]
    inputs += ["--input", "tester_yml=../actors/klee.yml"]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


def test_verifier_based_tester():
    inputs = ["verifier-based-tester.cvt"]
    inputs += ["--input", "program_path=test-data/c/CostasArray-10.c"]
    inputs += ["--input", "specification_path=test-data/properties/unreach-call.prp"]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


@pytest.mark.skip()
def test_repeat_condtest():
    inputs = ["CondTest/repeat-condtest.cvt"]
    inputs += ["--input", "program_path=test-data/c/Problem01_label15.c"]
    inputs += [
        "--input",
        "specification_path=test-data/properties/coverage-branches.prp",
    ]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


def test_metaval():
    inputs = ["MetaVal/metaval.cvt"]
    inputs += ["--input", "program_path=test-data/c/ConversionToSignedInt.i"]
    inputs += ["--input", "specification_path=test-data/properties/no-overflow.prp"]
    inputs += [
        "--input",
        "witness_path=test-data/witnesses/ConversionToSignedInt_nooverflow_witness.graphml",
    ]
    inputs += ["--input", "data_model=ILP32"]
    CoVeriTeam().start(inputs)


def test_multi_sequence_fase_22():
    inputs = ["--input", "program_path=test-data/c/Problem02_label16.c"]
    inputs += ["--input", "specification_path=test-data/properties/unreach-call.prp"]
    inputs += ["--input", "data_model=ILP32"]

    expected_verdict = extract_verdict_from_output(
        CoVeriTeam().start, ["FASE22/sequence-8.cvt"] + inputs
    )
    verdict = extract_verdict_from_output(
        CoVeriTeam().start, ["FASE22/sequence-8-with-new-sequence.cvt"] + inputs
    )
    assert expected_verdict == verdict


@pytest.mark.skip()
def test_multi_parallel_composition_fase_22():
    # Testing the construction of parallel composition with multiple arguments.
    inputs = ["--input", "program_path=test-data/c/Problem02_label16.c"]
    inputs += ["--input", "specification_path=test-data/properties/unreach-call.prp"]
    inputs += ["--input", "data_model=ILP32"]
    inputs += ["--input", "actordef_dir=FASE22/actor-definitions"]

    expected_verdict = extract_verdict_from_output(
        CoVeriTeam().start, ["FASE22/cst-selection-8.cvt"] + inputs
    )
    verdict = extract_verdict_from_output(
        CoVeriTeam().start, ["FASE22/cst-selection-8-with-new-parallel.cvt"] + inputs
    )
    assert expected_verdict == verdict
