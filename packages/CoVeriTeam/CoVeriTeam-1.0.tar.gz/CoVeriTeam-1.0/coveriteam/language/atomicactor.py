# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
import logging
import os
import uuid
from enum import Enum
from pathlib import Path
from string import Template
from typing import Dict, Optional
from xml.etree import ElementTree

import benchexec.containerexecutor as containerexecutor
from benchexec import tooladapter
from benchexec.container import DIR_HIDDEN, DIR_OVERLAY, DIR_READ_ONLY, DIR_FULL_ACCESS
from benchexec.model import cmdline_for_run, load_tool_info
from benchexec.runexecutor import RunExecutor
from benchexec.test_benchmark_definition import DummyConfig

from coveriteam import util
from coveriteam.language import CoVeriLangException
from coveriteam.language.actor import Actor
from coveriteam.language.actorconfig import ActorConfig
from coveriteam.language.artifact import AtomicActorDefinition, Program
from coveriteam.util import (
    TOOL_OUTPUT_FILE,
    str_dict,
    get_additional_paths_for_container_config,
    get_TOOL_INFO_DOWNLOAD_PATH,
)


def get_task_metadata(program: Optional[Program] = None) -> dict:
    """
    This function returns the task options to be passed to the tool info module
    to create a command.
    At the moment we only have two kinds of programs: C and Java.

    Args:
        program: A Program to analyze for metadata

    Returns:
        A dictionary which contains all necessary metadata for the given program. If no program or None is given, the dictionary is empty.
    """
    if not program:
        return {}
    d = {"language": program.get_language()}
    if program.data_model:
        d["data_model"] = program.data_model
    return d


class ExecutionState(Enum):
    Idle = 1  # Idling, not planned to start at the moment
    Preparing = 2  # In setup phase, RunExecutor not present
    Executing = 3  # Currently operating, thus able to stop with RunExecutor.stop()
    Stopping = 4  # Next scheduled execution will be stopped


def get_emtpy_measurements() -> Dict:
    """
    Returns a dictionary, which contains the minimum measurement data as keys.
    """
    return {
        "walltime": 0,
        "cputime": 0,
        "memory": 0,
    }


class AtomicActor(Actor):
    run_executor: RunExecutor
    execution_state: ExecutionState

    def __init__(self, path, version=None):
        super().__init__()
        self.execution_state = ExecutionState.Idle
        if isinstance(path, AtomicActorDefinition):
            path = path.path
        self.__config = ActorConfig(path, version)
        self.measurements = {}

    def name(self):
        return self.__config.actor_name

    def log_dir(self):
        # actor execution id is for the complete execution of an actor -- atomic or composite
        # atomic execution id is for this specific atomic actor.
        return (
            Actor.get_top_actor_execution_dir()
            / self.name()
            / self._atomic_execution_id
        )

    def log_file(self):
        return self.log_dir() / TOOL_OUTPUT_FILE

    def _get_relative_path_to_tool(self, path):
        return os.path.relpath(path, self.__config.tool_dir) if path else ""

    def print_version(self):
        cwd = os.getcwd()
        os.chdir(self.__config.tool_dir)
        self.__set_directory_modes({})

        tool_name = self.__config.tool_name or self.name()
        tool_info, self._tool = load_tool_info(
            tool_name, self.__create_config_for_container_execution()
        )
        tool_locator = tooladapter.CURRENT_BASETOOL.ToolLocator(
            use_path=True, use_current=True
        )
        version = self._tool.version(self._tool.executable(tool_locator))
        print(self._tool.name() + " " + version)
        os.chdir(cwd)

    def act(self, **kwargs):
        if self.execution_state is ExecutionState.Stopping:
            raise RuntimeError(
                f"act() called in {self.name()}, but it's trying to stop"
            )
        self.execution_state = ExecutionState.Preparing

        # Generate atomic execution id and then call the act method of the super class.
        self._atomic_execution_id = str(uuid.uuid4())
        self.__set_directory_modes(kwargs)
        res = super().act(**kwargs)

        return res

    def _act(self, **kwargs):
        args = self._prepare_args(**kwargs)
        # arg substitution is only for the options defined in the actor definitions
        d = self._get_arg_substitutions(**kwargs)
        options = [Template(o).safe_substitute(**d) for o in self.__config.options]
        task_options = get_task_metadata(kwargs.setdefault("program", None))
        try:
            self._run_tool(*args, options, task_options=task_options)
            res = self._extract_result()
            self._tool.close()
            return res
        except UnboundLocalError:
            msg = "The execution of the actor {} did not produce the expected result\n".format(
                self.name()
            )
            msg += "More information can be found in the logfile produced by the tool: {}".format(
                self.log_file()
            )
            raise CoVeriLangException(msg)
        finally:
            self.execution_state = ExecutionState.Idle

    def _run_tool(
        self,
        program_path,
        property_path,
        additional_options=[],
        options=[],
        task_options={},
    ):
        # Change directory to tool's directory
        cwd = os.getcwd()
        os.chdir(self.__config.tool_dir)

        if program_path:
            identifier = None
            if isinstance(program_path, str):
                program_path = [self._get_relative_path_to_tool(program_path)]
            elif isinstance(program_path, list):
                program_path = [
                    self._get_relative_path_to_tool(p) for p in program_path
                ]
        else:
            identifier = "no-program-file"

        property_path = self._get_relative_path_to_tool(property_path)

        tool_name = self.__config.tool_name or self.name()

        tool_info, self._tool = load_tool_info(
            tool_name, self.__create_config_for_container_execution()
        )
        lims_for_exec = {
            "softtimelimit": self.__config.reslim.get("timelimit"),
            "memlimit": self.__config.reslim.get("memlimit"),
        }
        resource_limits = tooladapter.CURRENT_BASETOOL.ResourceLimits(
            self.__config.reslim.get("timelimit"),
            self.__config.reslim.get("timelimit"),
            None,
            self.__config.reslim.get("memlimit"),
            self.__config.reslim.get("cpuCores"),
        )
        tool_locator = tooladapter.CURRENT_BASETOOL.ToolLocator(
            use_path=True, use_current=True
        )
        tool_executable = self._tool.executable(tool_locator)
        # TODO This is bad. It has to change. cmd should not be a part of the actor.
        # But we need it to extract result since PR 592 in benchexec.
        self._cmd = cmdline_for_run(
            self._tool,
            tool_executable,
            options + additional_options,
            program_path,
            identifier,
            property_path,
            task_options,
            resource_limits,
        )

        # Test for stopping the execution of this atomic actor
        self.run_executor = RunExecutor(dir_modes=self._dir_modes)

        logging.debug("RunExecutor created for %s", self.name())

        # Run stopped before actual execution, skipping execution
        if self.execution_state is ExecutionState.Stopping:
            self.measurements = get_emtpy_measurements()
            # State idle set later, after the processing of the measurements
            return

        self.execution_state = ExecutionState.Executing

        self.measurements = self.run_executor.execute_run(
            self._cmd,
            str(self.log_file().resolve()),
            output_dir=str(self.log_dir().resolve()),
            result_files_patterns=self._result_files_patterns,
            workingDir=self._tool.working_directory(tool_executable),
            environments=self._tool.environment(tool_executable),
            **lims_for_exec,
        )

        terminationreason = self.measurements.get("terminationreason")
        if terminationreason:
            logging.warning(
                "The actor %s was terminated by BenchExec. Termination reason: %s."
                " Possibly it did not produce the expected result.",
                self.name(),
                terminationreason,
            )

        # Change back to the original directory
        os.chdir(cwd)

    def gen_xml_elem(self, inputs, outputs, **kwargs):
        super().gen_xml_elem(inputs, outputs, **kwargs)
        data = self.get_measurements_data_for_xml()
        self.xml_elem.append(ElementTree.Element("measurements", str_dict(data)))
        tool_output_elem = ElementTree.Element("tool_output")
        tool_output_elem.text = str(Actor._get_relative_path_to_actor(self.log_file()))
        self.xml_elem.append(tool_output_elem)

    def get_measurements_data_for_xml(self):
        data_filter = ["cputime", "walltime", "memory"]
        data = {k: self.measurements[k] for k in data_filter if k in self.measurements}
        return str_dict(data)

    def __set_directory_modes(self, inputs):
        # The default directory modes taken from container executor.
        self._dir_modes = {
            "/": DIR_READ_ONLY,
            "/run": DIR_HIDDEN,
            "/tmp": DIR_HIDDEN,  # noqa S108
        }
        # Update the default with the /sys and /home as hidden.
        self._dir_modes["/sys"] = DIR_HIDDEN
        self._dir_modes["/home"] = DIR_HIDDEN
        if Actor.allow_cgroup_access:
            self._dir_modes["/sys/fs/cgroup"] = DIR_FULL_ACCESS

        self._dir_modes[util.get_CACHE_DIR_PATH()] = DIR_READ_ONLY
        self._dir_modes[self.__config.tool_dir] = DIR_OVERLAY
        self._dir_modes[str(get_TOOL_INFO_DOWNLOAD_PATH())] = DIR_OVERLAY

        for v in inputs.values():
            if isinstance(v.path, str):
                p = str(Path(v.path).parent.resolve())
                self._dir_modes[p] = DIR_READ_ONLY
            elif isinstance(v.path, list):
                for path in v.path:
                    p = str(Path(path).parent.resolve())
                    self._dir_modes[p] = DIR_READ_ONLY

    def __create_config_for_container_execution(self):
        try:
            if Actor.trust_tool_info:
                return DummyConfig
        except AttributeError:
            # We use the standard container config if the field doesn't exist.
            pass

        parser = argparse.ArgumentParser()
        containerexecutor.add_basic_container_args(parser)
        containerexecutor.add_container_output_args(parser)
        mp = {
            DIR_HIDDEN: "--hidden-dir",
            DIR_OVERLAY: "--overlay-dir",
            DIR_READ_ONLY: "--read-only-dir",
            DIR_FULL_ACCESS: "--full-access-dir",
        }
        args = []
        for p in get_additional_paths_for_container_config():
            args += ["--full-access-dir", p]
        for k, v in self._dir_modes.items():
            args += [mp[v], k]
        config = parser.parse_args(args)
        config.container = True
        return config

    def _get_arg_substitutions(self, **kwargs):
        return {}

    def stop(self):
        logging.debug("Shutting down atomic actor: %s", self.name())
        if self.execution_state is ExecutionState.Executing:
            # RunExecutor is present
            self.run_executor.stop()
        elif self.execution_state is ExecutionState.Preparing:
            # No RunExecutor present, next execution will be skipped
            self.execution_state = ExecutionState.Stopping
        elif self.execution_state is ExecutionState.Stopping:
            logging.info("stop() called in %s, but it is already stopping", self.name())
        else:
            logging.info("stop() called in %s, ignored because of idling", self.name())
