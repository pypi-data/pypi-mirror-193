# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import filecmp
import logging
import os
import shutil
import time
import uuid
import xml.etree.ElementTree as ET  # noqa N817 use of idiomatic name ET for ElementTree
from pathlib import Path
from typing import Optional, List, Union

from benchexec.result import get_result_classification

from coveriteam.language import CoVeriLangException
from coveriteam.language import witness_join, predmap_join

VERDICT_TRUE = "TRUE"
VERDICT_FALSE = "FALSE"
VERDICT_UNKNOWN = "UNKNOWN"
VERDICT_ERROR = "ERROR"
VERDICT_TIMEOUT = "TIMEOUT"


class Artifact:
    def __init__(self, path: Optional[str] = None):
        if path:
            self.path = str(Path(path).resolve())
        else:
            self.path = ""

    def __str__(self):
        return os.path.relpath(self.path, os.getcwd()) if self.path else ""

    def __repr__(self):
        return "'%s'" % os.path.relpath(self.path, os.getcwd()) if self.path else ""

    def get_default_artifact(self):
        raise NotImplementedError(f"Empty artifact not implemented in {self.__class__}")


class Joinable:
    def join(self, artifact2):
        """
        Definition of this function is to be provided by the child class.
        """
        pass


class Comparable:
    def compare(self, artifact2):
        """
        Definition of this function is to be provided by the child class.
        """
        pass


class BehaviorDescription(Artifact):
    pass


class Justification(Artifact):
    pass


class Verdict(Artifact):
    def __init__(self, verdict: str):
        super().__init__()
        self.verdict = verdict
        self.path = ""

    def __str__(self):
        return self.verdict

    def __repr__(self):
        return "'%s'" % self.verdict

    def __eq__(self, other):
        # Compare only true or false. We can see later if we need to compare the actual string.
        if type(other) is str:
            return get_result_classification(self.verdict) == get_result_classification(
                other
            )

        if isinstance(other, Verdict):
            return get_result_classification(self.verdict) == get_result_classification(
                other.verdict
            )

        raise CoVeriLangException(
            f"Error while comparing Verdict with object of type {type(other)}"
        )

    def get_default_artifact(self):
        return Verdict(VERDICT_UNKNOWN)


class Specification(Artifact):
    pass


class Program(BehaviorDescription):
    # TODO move it to artifact at some point
    def __init__(
        self, path: Optional[Union[str, list]] = None, data_model: Optional[str] = None
    ):
        super().__init__()
        self.multipath = not isinstance(path, str) and isinstance(path, list)
        if self.multipath:
            if self.multipath_allowed():
                self.path = [str(Path(path_string).resolve()) for path_string in path]
            else:
                raise CoVeriLangException(
                    "Multiple paths not allowed for %s programs." % self.get_language()
                )
        else:
            self.path = str(Path(path).resolve())

        self.data_model = None
        if self.data_model_required():
            if data_model:
                self.data_model = data_model
            else:
                # Warning might be changed to raising an error
                logging.warning("Data Model missing for program %s. Taking ILP32", path)
                self.data_model = "ILP32"
        elif data_model:
            raise CoVeriLangException(
                "Data model is not allowed in %s verification." % self.get_language()
            )

    def __str__(self):
        if self.multipath:
            return str(
                [os.path.relpath(p, os.getcwd()) if p else "" for p in self.path]
            )
        return super().__str__()

    def __repr__(self):
        if self.multipath:
            return str(
                [
                    "'%s'" % os.path.relpath(p, os.getcwd()) if p else ""
                    for p in self.path
                ]
            )
        return super().__repr__()

    def multipath_allowed(self):
        """
        Checks if the multiple paths are allowed or not.

        Returns:
            True, if this multiple paths are allowed.
        """
        raise NotImplementedError("Not implemented in %s" % self.__class__)

    def data_model_required(self) -> bool:
        """
        Returns the need of a data model for this program

        Returns:
            True, if this program needs a data model
        """
        raise NotImplementedError("Not implemented in %s" % self.__class__)

    def get_language(self) -> str:
        """
        Returns the language this program is written in

        Returns:
            str, name of the programming language
        """
        raise NotImplementedError("Not implemented in %s" % self.__class__)

    @staticmethod
    def create(
        path: Union[str, List[str]], data_model: Optional[str] = None
    ) -> "Program":
        """
        Factory method to create new programs.
        Previously we accepted programs with an empty path. Now one or multiple file paths must be given

        Args:
            path: A single or list of path like strings
            data_model: The data model given as string, choice of {"ILP32", "LP64"}
        """
        if isinstance(path, str):
            if Path(path).resolve().suffix in [".i", ".c"]:
                return CProgram(path, data_model)
            return JavaProgram(path)

        if isinstance(path, list):
            return JavaProgram(path)

        raise CoVeriLangException("Can't read program with path %s" % path)


class CProgram(Program):
    def multipath_allowed(self):
        return False

    def data_model_required(self) -> bool:
        return True

    def get_language(self):
        return "C"


class JavaProgram(Program):
    def multipath_allowed(self):
        return True

    def data_model_required(self) -> bool:
        return False

    def get_language(self) -> str:
        return "Java"


class BehaviorSpecification(Specification):
    pass


class TestSpecification(Specification):
    pass


class Predicates(Artifact, Joinable):
    """
    A collection of predicates that can be used to describe a (probably relevant)
    state space of a system.
    Predicates are often boolean formulas over program variables and literals,
    and are sometimes limited to a certain program scope.
    """

    def timestamp(self):
        return str(time.time())

    def join(self, other):
        assert type(self) is type(
            other
        ), "Cannot join %r and %r. Types are not same." % (self, other)
        if not self.path:
            assert isinstance(other, Predicates)
            return other
        if not other.path:
            return self
        joined = Path(self.path).parent / (
            "predmap-joined." + self.timestamp() + ".txt"
        )
        predmap_join.merge_predmap(
            first_path=self.path, second_path=other.path, target_path=joined
        )
        assert joined.exists(), "Path was not created: " + str(joined)
        return Predicates(joined)


class Witness(Justification, Joinable):
    def join(self, other):
        assert type(self) is type(
            other
        ), "Cannot join %r and %r. Types are not same." % (self, other)
        if not self.path:
            return Witness(other.path)
        if not other.path:
            return self
        joined = Path(self.path).parent / (str(uuid.uuid4()) + ".graphml")
        witness_join.merge_witnesses(
            first_path=self.path, second_path=other.path, target_path=joined
        )
        assert joined.exists(), "Path was not created: " + str(joined)
        return Witness(joined)

    def __eq__(self, other):
        if isinstance(other, Witness):
            if self.path and other.path:
                with open(self.path) as inp:
                    content1 = inp.read()
                with open(other.path) as inp:
                    content2 = inp.read()
                if content1 == content2:
                    return True
                return Witness._semantic_equivalence(content1, content2)
            if not self.path and not other.path:
                return True
        return False

    def get_default_artifact(self):
        return Witness("")

    @staticmethod
    def _semantic_equivalence(witness1, witness2):
        def parse(witness):
            try:
                root = ET.fromstring(witness)  # noqa S314 insecure, but included
            except ET.ParseError:
                root = ET.parse(witness).getroot()  # noqa S314 insecure, but included
            if root.tag == "{http://graphml.graphdrawing.org/xmlns}graph":
                return root
            return root.find("{http://graphml.graphdrawing.org/xmlns}graph")

        def get_type(graph):
            type_data = next(
                (
                    data
                    for data in graph.findall("data")
                    if data.attrib["key"] == "witness-type"
                ),
                None,
            )
            return not type_data or type_data.text

        def get_invariants(graph):
            invs = []
            for node in graph.findall("{http://graphml.graphdrawing.org/xmlns}node"):
                invs += [
                    data
                    for data in node.findall(
                        "{http://graphml.graphdrawing.org/xmlns}data"
                    )
                    if data.attrib["key"] == "invariant"
                ]
            return invs

        ET.register_namespace("", "http://graphml.graphdrawing.org/xmlns")
        ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
        graph1 = parse(witness1)
        graph2 = parse(witness2)

        if graph1 is None or graph2 is None:
            logging.info("Graph is none: %s, %s", graph1, graph2)
            return True
        if get_type(graph1) != get_type(graph2):
            logging.info("Invalid types")
            return False

        invariants1 = get_invariants(graph1)
        invariants2 = get_invariants(graph2)

        logging.info("Invariant length: %s, %s", len(invariants1), len(invariants2))
        if len(invariants1) != len(invariants2):
            return False

        # check both directions to get complete matching: each inv in invariants1
        # must have match in invariants2, and each inv in invariants2
        # must have match in invariants1
        for outer, inner in ((invariants1, invariants2), (invariants2, invariants1)):
            for inv1 in outer:
                formula1 = inv1.text
                for inv2 in inner:
                    formula2 = inv2.text
                    if formula1 == formula2:
                        break
                else:
                    return False
        return True


class ReachabilityWitness(Witness):
    pass


class Condition(Justification):
    pass


class TestGoal(Condition, Joinable):
    def join(self, other):
        assert type(self) is type(
            other
        ), "Cannot join %r and %r. Types are not same." % (self, other)
        if not self.path:
            return TestGoal(other.path)

        if other.path:
            # If files are same then no need to compare
            if filecmp.cmp(self.path, other.path, False):
                return self
            joined = Path(self.path).parent / str(uuid.uuid4())
            with joined.open("w") as f:
                with open(self.path) as f1:
                    f.write(f1.read())
                with open(other.path) as f1:
                    f.write(f1.read())
            return TestGoal(joined)
        # When other does not exist
        return self

    def __eq__(self, other):
        if isinstance(other, TestGoal):
            if self.path and other.path:
                return filecmp.cmp(self.path, other.path, False)
            if not (self.path or other.path):
                return True
            return False
        return False


class TestSuite(Justification):
    def join(self, other):
        assert type(self) is type(
            other
        ), "Cannot join %r and %r. Types are not same." % (self, other)
        if not self.path:
            self.path = other.path
        elif other.path:
            shutil.copytree(other.path, str(Path(self.path) / str(uuid.uuid4())))
        return self


class AtomicActorDefinition(Artifact):
    def __init__(self, actordef, actordef_dir=""):
        super().__init__()
        self.actordef = actordef
        # Assumption: There should be a file present with the same name in our actor configs.
        if actordef_dir:
            actordef_dir = Path(actordef_dir)
        else:
            this_path = Path(__file__).resolve()
            actordef_dir = this_path.parent.parent.parent / "actors"

        actordef_path = actordef_dir / (actordef + ".yml")

        if actordef_path.exists():
            self.path = str(actordef_path)
        else:
            raise Exception("Actor %r could not be found!!" % actordef)

    def __str__(self):
        return self.actordef


class FeatureVector(Artifact):
    # TODO check if it should inherit from Artifact or something else
    pass


class ClassificationConfidence(Artifact, Comparable):
    # TODO:
    #   1. convert to XML for execution trace
    #   2. printing out multi field artifacts that are not based on path
    def __init__(self, clazz, confidence):
        self.clazz = clazz
        self.confidence = confidence
        self.path = ""

    def compare(self, artifact2):
        if float(self.confidence) > float(artifact2.confidence):
            return self
        return artifact2

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return str(vars(self))

    def __gt__(self, artifact2):
        return float(self.confidence) > float(artifact2.confidence)


class ActorDefinitionDirectory(Artifact):
    def __init__(self, path):
        self.path = path

    def get_default_artifact(self):
        return ActorDefinitionDirectory("")
