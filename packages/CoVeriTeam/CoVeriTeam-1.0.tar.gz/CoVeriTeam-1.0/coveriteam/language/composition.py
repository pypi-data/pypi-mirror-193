# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import multiprocessing
import signal
from textwrap import indent
from typing import Any
from xml.etree import ElementTree

# TODO find a better way to do this
from benchexec.result import RESULT_CLASS_FALSE  # noqa: F401,F403,E261
from benchexec.result import RESULT_CLASS_OTHER  # noqa: F401,F403,E261
from benchexec.result import RESULT_CLASS_TRUE  # noqa: F401,F403,E261

from coveriteam import util
from coveriteam.language.actor import Actor
from coveriteam.language.artifact import *  # noqa: F401,F403,E261
from coveriteam.util import (
    filter_dict,
    artifact_name_clash,
    collect_variables,
    CVT_DEBUG_LEVEL,
)


def infer_types(exp):
    d = {}
    # TODO At the moment it is rudimentory. Putting Artifact for everything
    for name in collect_variables(exp):
        if not name.startswith("RESULT_CLASS"):
            d[name] = Artifact

    return d


class CompositeActor(Actor):
    def __init__(self):
        super().__init__()

    def name(self):
        try:
            return self._name
        except AttributeError:
            return type(self).__name__

    def set_name(self, name):
        # This is only in the composite actor.
        # The names of the atomic actors come from the actor definition.
        self._name = name

    def forward_artifacts(self, available, renaming, required):
        """
        This function does two things:
        1) Selects the artifacts to be passed to a subcomponent from the available
           artifacts.
        2) Applies renaming if neccessary.
        """
        # TODO at the moment renaming is not considered
        return filter_dict(available, required)


def set_composite_actor_name(actor, name):
    if isinstance(actor, CompositeActor):
        actor.set_name(name)
    else:
        raise CoVeriLangException(
            "Setting name is only supported for composite actors."
        )


class Sequence(CompositeActor):
    def __init__(self, actor_list: List[Actor]):
        super().__init__()
        self.actors = actor_list
        self._input_artifacts = self._infer_input_type()
        self._output_artifacts = self.actors[-1].get_output_artifacts()
        self.__type_check()
        logging.log(
            CVT_DEBUG_LEVEL,
            f"Created SEQUENCE with inputs {self._input_artifacts} and outputs {self._output_artifacts}",
        )

    def _act(self, **kwargs):
        result = {}
        for actor in self.actors:
            # This is ugly, but it works
            args = self.forward_artifacts(
                {**kwargs, **result}, {}, actor.get_input_artifacts()
            )
            result = actor.act(**args)

        return result

    def __type_check(self):
        for index, actor in enumerate(self.actors):
            # Skipping of first actor, because all his inputs are in the sequence input
            if index == 0:
                continue
            pre_actor = self.actors[index - 1]

            # Building the dict of all available inputs for the current actor
            dict_to_check = {**self._input_artifacts}
            dict_to_check.update(pre_actor.get_output_artifacts())

            if util.artifact_name_clash(actor.get_input_artifacts(), dict_to_check):
                raise CoVeriLangException(
                    "Components {} \n and \n {} cannot be composed in sequence."
                    "Type check failed.".format(pre_actor, actor)
                )

    def __str__(self):
        return (
            "\nSEQUENCE"
            + self.__get_actor_type_str__()
            + "\n"
            + "\n".join([indent(str(actor), "\t") for actor in self.actors])
        )

    def gen_xml_elem(self, inputs, outputs, **kwargs):
        super().gen_xml_elem(inputs, outputs, **kwargs)

        for index, actor in enumerate(self.actors):
            element = ElementTree.Element("actor_" + str(index))
            append_xml_elem_if_exists(element, actor)
            self.xml_elem.append(element)

    def _infer_input_type(self):
        inputs = {**self.actors[0].get_input_artifacts()}

        for index, actor in enumerate(self.actors):
            if index == 0:
                continue

            # All keys, which are not already in the outputs of the actor before
            keys_to_add = {
                k: v
                for k, v in actor.get_input_artifacts().items()
                if k not in self.actors[index - 1].get_output_artifacts()
            }
            # Selecting the minimum type for the key in inputs
            # For example, Verdict < Artifact, therefore choose Verdict
            inputs.update(
                {
                    k: util.specific_type_selector(
                        inputs.get(k, Artifact), keys_to_add.get(k, Artifact)
                    )
                    for k, v in keys_to_add.items()
                }
            )

        return inputs

    def stop(self):
        for actor in self.actors:
            actor.stop()


class ITE(CompositeActor):
    """Concerns faced:
    1) the condition might need a variable which is not required by the composing actors.
    -- To avoid this at the moment it is allowd that the inputs could be more than
    required by the composing actors."""

    def __init__(self, cond, a1, a2=None):
        super().__init__()
        self.cond = cond
        self.first = a1
        self.second = a2
        if a2 and a2.get_input_artifacts():
            self._input_artifacts = {
                **a1.get_input_artifacts().copy(),
                **a2.get_input_artifacts().copy(),
            }
        else:
            self._input_artifacts = a1.get_input_artifacts().copy()
        self._output_artifacts = a1.get_output_artifacts().copy()
        self._add_types_from_cond(cond)
        self.__type_check(a1, a2)

    def _act(self, **kwargs):
        # Tried using ast.literal_eval but couldn't use it. Still check it once more
        # noqa because can't pass kwargs to ast.literal_eval
        cond_val = eval(self.cond, globals(), {**kwargs})  # noqa: S307
        if cond_val:
            args_to_pass = self.forward_artifacts(
                kwargs, {}, self.first.get_input_artifacts()
            )
            ret_val = self.first.act(**args_to_pass)
        elif self.second:
            # TODO check if this and the one in if condition are same
            args_to_pass = self.forward_artifacts(
                kwargs, {}, self.second.get_input_artifacts()
            )
            ret_val = self.second.act(**args_to_pass)
        else:
            # In this case the values from the inputs are forwarded.
            ret_val = filter_dict(kwargs, keys_to_keep=self._output_artifacts)

        return ret_val

    def __type_check(self, a1, a2):
        # TODO need to check covariance here.
        if not a2:
            pass
            if not (a1.get_output_artifacts().items() <= self._input_artifacts.items()):
                # In this case we still would like to check if the inputs could be forwarded.
                raise CoVeriLangException(
                    "Type check failed for ITE composition."
                    " Input types must be a super set of the output types defined by the if-actor,"
                    " because no else-actor is defined."
                    "\nInputs: {}\nOutputs of if-actor: {}".format(
                        self._input_artifacts, a1.get_output_artifacts()
                    )
                )
        elif a1.get_output_artifacts() != a2.get_output_artifacts():
            raise CoVeriLangException(
                "Components\n {}\n and\n {} cannot be composed in ITE:"
                "Output types of if-actor and else-actor do not match:\n"
                "Outputs of if-actor: {}"
                "Outputs of else-actor: {}".format(
                    a1, a2, a1.get_output_artifacts(), a2.get_output_artifacts()
                )
            )

    def __str__(self):
        return (
            "\nITE"
            + self.__get_actor_type_str__()
            + "\n"
            + indent(str(self.first), "\t")
            + "\n"
            + indent(str(self.second), "\t")
        )

    def gen_xml_elem(self, inputs, outputs, cond_val=None, **kwargs):
        super().gen_xml_elem(inputs, outputs, **kwargs)
        cond_elem = ElementTree.Element("condition")
        cond_elem.text = str(cond_val)
        self.xml_elem.append(cond_elem)
        if cond_val:
            append_xml_elem_if_exists(self.xml_elem, self.first)
        elif self.second:
            append_xml_elem_if_exists(self.xml_elem, self.second)

    def _add_types_from_cond(self, cond):
        t = infer_types(cond)
        self._input_artifacts = {**t, **self._input_artifacts}

    def stop(self):
        self.first.stop()
        if self.second is not None:
            self.second.stop()


class Iterative(CompositeActor):
    is_stop: bool

    # I think every can be run iteratively. Two cases arise which need to be handled:
    # 1) What if all the outputs are disregarded - It is still a valid composition
    # 2) if outputs are to be fed to inputs but have different names
    def __init__(self, termination_condition, a: Actor):
        super().__init__()
        self.is_stop = False
        self.__type_check(a)
        self.actor = a
        self.termination_condition = termination_condition
        self._input_artifacts = a.get_input_artifacts()
        self._output_artifacts = a.get_output_artifacts()
        # TODO This is making it stateful, might create a problem later.
        self._iteration_count = 0
        self.__child_xml_elems = []
        # TODO Put it in type check too
        self.__artifacts_to_accumulate = []
        self.__accumulated_artifacts = {}
        logging.log(
            CVT_DEBUG_LEVEL,
            f"Created CYCLE with inputs {self._input_artifacts} and outputs {self._output_artifacts}",
        )

    def _act(self, **kwargs):
        # TODO Maybe it is a better idea to keep all the objects as they go along.
        # This might solve the xml generation issues.
        res = self.actor.act(**kwargs)
        self.__do_step_iteration_post_process(kwargs, res)
        # BEWARE!! to think if it is OK. This is out of syn with the paper.
        # We have said that inputs are subset of outputs, but here we don't necessarily assume that.

        newargs = {**kwargs, **res}
        if self.__check_termination_condition(kwargs, res):
            updated_args = {**newargs, **self.__accumulated_artifacts}
            ret_val = self.forward_artifacts(
                updated_args, {}, self.actor.get_output_artifacts()
            )
        else:
            args_to_pass = self.forward_artifacts(
                newargs, {}, self.actor.get_input_artifacts()
            )
            ret_val = self.act(**args_to_pass)

        self.gen_xml_elem(
            self.__initial_inputs,
            self.forward_artifacts(newargs, {}, self.actor.get_output_artifacts()),
        )
        logging.log(
            CVT_DEBUG_LEVEL, f"CYCLE iteration count: {self._iteration_count - 1}"
        )
        return ret_val

    def __type_check(self, a):
        """
        In iterative composition the type check only checks if there is at least one
        artifact which can be fed back to the actor.
        Other artifacts retain their initial values.
        """
        inputs = a.get_input_artifacts().items()
        outputs = a.get_output_artifacts().items()
        # TODO TK: Check with Sudeep, what to do here
        if not (a.get_input_artifacts().keys() & a.get_output_artifacts().keys()):
            raise CoVeriLangException(
                "Type check failed:"
                " Component cannot be composed with itself for iteration"
                " because there is no output artifact that is also expected as input."
                " Inputs vs outputs:\n{}\nvs.\n{}\n>> Component start:\n{}\n>> Component end".format(
                    inputs, outputs, a
                )
            )

    def __check_termination_condition(self, kwargs, res):
        # Lets see if it is enough or we need to make it more expressive.
        tc_val = eval(  # noqa: S307
            self.termination_condition, globals(), {**kwargs, **res}
        )
        if tc_val:
            logging.info("Terminating cycle because %s evaluates to True", tc_val)
        return tc_val or self.is_stop

    def __do_step_iteration_post_process(self, it_input, it_output):
        self.__collect_xml_elems(it_input)

        # Collect artifacts
        for k in self.__artifacts_to_accumulate:
            if k in self.__accumulated_artifacts:
                self.__accumulated_artifacts[k] = self.__accumulated_artifacts[k].join(
                    it_output[k]
                )
            else:
                self.__accumulated_artifacts[k] = it_output[k]

    def __collect_xml_elems(self, inputs):
        if self._iteration_count == 0:
            self.__initial_inputs = inputs
        it_elem = ElementTree.Element(
            "Iteration", {"count": str(self._iteration_count)}
        )
        append_xml_elem_if_exists(it_elem, self.actor)
        self.__child_xml_elems.append(it_elem)
        self._iteration_count += 1

    def gen_xml_elem(self, inputs, outputs, **kwargs):
        super().gen_xml_elem(inputs, outputs, **kwargs)

        for i in self.__child_xml_elems:
            self.xml_elem.append(i)

    def __str__(self):
        return (
            "\nREPEAT"
            + self.__get_actor_type_str__()
            + "\n"
            + indent(str(self.actor), "\t")
        )

    def stop(self):
        self.is_stop = True
        self.actor.stop()


def parallel_execution_helper(
    actor: Actor, actor_id: int, actor_kwargs, shared_dict: dict
):
    # Creating signal handlers to react on shutdown signal from main thread and KeyboardInterrupt
    for sig in [signal.SIGTERM, signal.SIGINT]:
        signal.signal(sig, lambda s, h: actor.stop())

    shared_dict[actor_id] = (actor.act(**actor_kwargs), actor.xml_elem)


class Parallel(CompositeActor):
    def __init__(self, actor_list: List[Actor]):
        super().__init__()
        self.__type_check(actor_list)
        self.actors: List[Actor] = actor_list
        self.processes = []

        self._input_artifacts = util.get_type_per_key_dict_list(
            [actor.get_input_artifacts() for actor in self.actors],
            util.specific_type_selector,
        )
        self._output_artifacts = util.get_type_per_key_dict_list(
            [actor.get_output_artifacts() for actor in self.actors],
            util.generic_type_selector,
        )
        logging.log(
            CVT_DEBUG_LEVEL,
            f"Created PARALLEL with inputs {self._input_artifacts} and outputs {self._output_artifacts}",
        )

    def _act(self, **kwargs):
        # TODO It might not work as the arguments passed are more than required
        # TODO project the arguments as required

        manager = multiprocessing.Manager()
        shared_dict = manager.dict()

        self.processes = [
            multiprocessing.Process(
                target=parallel_execution_helper,
                args=(
                    actor,
                    actor_id,
                    self.forward_artifacts(kwargs, {}, actor.get_input_artifacts()),
                    shared_dict,
                ),
            )
            for actor_id, actor in enumerate(self.actors)
        ]

        for process in self.processes:
            process.start()
        for process in self.processes:
            process.join()

        ret_val = {}
        for actor_id, actor in enumerate(self.actors):
            actor_res, actor.xml_elem = shared_dict[actor_id]
            ret_val.update(actor_res)

        manager.shutdown()
        self.gen_xml_elem(kwargs, ret_val)
        return ret_val

    def __type_check(self, actor_list: List[Actor]):
        if len(actor_list) < 2:
            return
        current_actor = actor_list[0]
        for actor in actor_list[1:]:
            # Check for dict_clash with every remaining actor
            if artifact_name_clash(
                current_actor.get_input_artifacts(),
                actor.get_input_artifacts(),
                allow_both_directions=True,
            ):
                raise CoVeriLangException(
                    "Components \n {} \n and \n {} \ncannot be composed in parallel. "
                    "Input names clash. There is an input with the same name and "
                    "different artifact type. Type check failed.".format(
                        current_actor, actor
                    )
                )

            # Names in outputs can not be defined twice
            if (
                not current_actor.get_output_artifacts()
                .keys()
                .isdisjoint(actor.get_output_artifacts())
            ):
                raise CoVeriLangException(
                    "Components \n{} \nand \n {} \ncannot be composed in parallel. "
                    "Output names should be disjoint. Type check failed.".format(
                        current_actor, actor
                    )
                )
        self.__type_check(actor_list[1:])

    def __str__(self):
        return (
            "\nPARALLEL"
            + self.__get_actor_type_str__()
            + "\n"
            + "\n".join([indent(str(actor), "\t") for actor in self.actors])
        )

    def gen_xml_elem(self, inputs, outputs, **kwargs):
        super().gen_xml_elem(inputs, outputs, **kwargs)
        for actor in self.actors:
            append_xml_elem_if_exists(self.xml_elem, actor)

    def stop(self):
        for process in self.processes:
            process.terminate()


def append_xml_elem_if_exists(elements: list, owner: Any):
    if owner.xml_elem:
        elements.append(owner.xml_elem)
