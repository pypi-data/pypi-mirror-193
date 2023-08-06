# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

from coveriteam.language.actor import Transformer, Verifier, Validator
from coveriteam.language.atomicactor import AtomicActor
from coveriteam.language.artifact import (
    Program,
    Specification,
    Witness,
    Verdict,
    TestSuite,
    TestSpecification,
    Predicates,
    AtomicActorDefinition,
)
import logging
from pathlib import Path
from typing import Optional
from coveriteam.language import CoVeriLangException
from coveriteam.util import create_archive
from benchexec import tooladapter
from benchexec.result import get_result_classification
import os


def extract_verdict(self):
    try:
        with open(self.log_file(), "rt", errors="ignore") as outputFile:
            output = outputFile.readlines()
            # first 6 lines are for logging, rest is output of subprocess, see runexecutor.py for details
            output = output[6:]
    except IOError as e:
        logging.warning("Cannot read log file: %s", e.strerror)
        output = []

    exit_code = self.measurements.get("exitcode")
    output = tooladapter.CURRENT_BASETOOL.RunOutput(output)
    run = tooladapter.CURRENT_BASETOOL.Run(self._cmd, exit_code, output, None)

    return Verdict(self._tool.determine_result(run))


def extract_witness(self, pattern):
    path = extract_artifact(self, pattern)
    if path is None:
        return Witness("")
    return Witness(path)


def extract_predicates(self, pattern):
    path = extract_artifact(self, pattern)
    if path is None:
        return Predicates("")
    return Predicates(path)


def extract_artifact(self, pattern: str) -> Optional[Path]:
    artifact_list = list(self.log_dir().glob(pattern))

    if not artifact_list:
        return None

    if len(artifact_list) != 1:
        msg = (
            "Found more than one artifact matching pattern. Following are the artifacts found: \n"
            + "\n".join(map(str, artifact_list))
        )
        raise CoVeriLangException(msg)

    return artifact_list[0]


class ProgramVerifier(Verifier, AtomicActor):
    _input_artifacts = {"program": Program, "spec": Specification}
    _output_artifacts = {"verdict": Verdict, "witness": Witness}
    _result_files_patterns = ["**/*.graphml"]

    # It is a deliberate decision to not have the init function. We do not want anyone to
    # create instances of this class.

    def _prepare_args(self, program, spec):
        return [program.path, spec.path]

    def _extract_result(self):
        witness = extract_witness(self, "**/*.graphml")
        verdict = extract_verdict(self)
        verdict_class = get_result_classification(verdict.verdict)
        if not witness.path and verdict_class in ("true", "false"):
            verdict = Verdict("VERDICT_DISCARDED(NO WITNESS)")

        return {
            "verdict": verdict,
            "witness": witness,
        }


class CoVeriTeamBasedProgramVerifier(ProgramVerifier):
    _input_artifacts = {
        "program": Program,
        "spec": Specification,
        "verifier_config_to_use": AtomicActorDefinition,
    }

    def _prepare_args(self, program, spec, verifier_config_to_use):
        return [program.path, spec.path]

    def _get_arg_substitutions(self, program, spec, verifier_config_to_use):
        return {"verifier_config_to_use": str(verifier_config_to_use)}

    def _extract_last_witness(self):
        artifact_list = list(self.log_dir().glob("**/*.graphml"))
        if not artifact_list:
            artifact_list = [""]
        return Witness(artifact_list[-1])

    def _extract_result(self):
        return {
            "verdict": extract_verdict(self),
            "witness": self._extract_last_witness(),
        }


class PredicateBasedProgramVerifier(ProgramVerifier):
    _input_artifacts = {
        "program": Program,
        "spec": Specification,
        "predicates": Predicates,
    }
    _output_artifacts = {
        "verdict": Verdict,
        "witness": Witness,
        "predicates": Predicates,
    }
    _result_files_patterns = ["**/*.graphml", "**/predmap.txt"]

    # It is a deliberate decision to not have the init function. We do not want anyone to
    # create instances of this class.
    def _get_arg_substitutions(self, program, spec, predicates):
        return {"predicates": self._get_relative_path_to_tool(predicates.path)}

    def _prepare_args(self, program, spec, predicates):
        return [program.path, spec.path]

    def _extract_result(self):
        return {
            "verdict": extract_verdict(self),
            "witness": extract_witness(self, "**/*.graphml"),
            "predicates": extract_predicates(self, "**/predmap.txt"),
        }


class ProgramValidator(Validator, AtomicActor):
    _input_artifacts = {
        "program": Program,
        "spec": Specification,
        "witness": Witness,
        "verdict": Verdict,
    }
    _output_artifacts = {"verdict": Verdict, "witness": Witness}
    _result_files_patterns = ["**/*.graphml"]

    def _get_arg_substitutions(self, program, spec, witness, verdict):
        return {"witness": self._get_relative_path_to_tool(witness.path)}

    def _prepare_args(self, program, spec, witness, verdict):
        return [program.path, spec.path]

    def _extract_result(self):
        return {
            "verdict": extract_verdict(self),
            "witness": extract_witness(self, "**/*.graphml"),
        }


class PredicateBasedProgramValidator(ProgramValidator):
    _input_artifacts = {
        "program": Program,
        "spec": Specification,
        "witness": Witness,
        "verdict": Verdict,
        "predicates": Predicates,
    }
    _output_artifacts = {
        "verdict": Verdict,
        "witness": Witness,
        "predicates": Predicates,
    }
    _result_files_patterns = ["**/*.graphml", "**/predmap.txt"]

    # It is a deliberate decision to not have the init function. We do not want anyone to
    # create instances of this class.

    def _get_arg_substitutions(self, program, spec, witness, verdict, predicates):
        return {
            "witness": self._get_relative_path_to_tool(witness.path),
            "predicates": self._get_relative_path_to_tool(predicates.path),
        }

    def _prepare_args(self, program, spec, witness, verdict, predicates):
        return [program.path, spec.path]

    def _extract_result(self):
        return {
            "verdict": extract_verdict(self),
            "witness": extract_witness(self, "**/*.graphml"),
            "predicates": extract_predicates(self, "**/predmap.txt"),
        }


class TestValidator(Transformer, AtomicActor):
    _input_artifacts = {
        "program": Program,
        "test_suite": TestSuite,
        "test_spec": TestSpecification,
    }
    _output_artifacts = {"verdict": Verdict}
    _result_files_patterns = []

    def _prepare_args(self, program, test_suite, test_spec):
        options_spec = ["--goal", self._get_relative_path_to_tool(test_spec.path)]
        testzip = os.path.join(os.path.dirname(test_suite.path), "test_suite.zip")
        create_archive(test_suite.path, testzip)
        testzip = self._get_relative_path_to_tool(testzip)
        options_test_suite = ["--test-suite", testzip]
        options = options_test_suite + options_spec
        return [program.path, "", options]

    def _extract_result(self):
        return {"verdict": extract_verdict(self)}
