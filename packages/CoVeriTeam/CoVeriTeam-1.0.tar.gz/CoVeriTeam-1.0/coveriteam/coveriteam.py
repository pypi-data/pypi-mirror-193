# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0
import argparse
import collections
import logging
import shutil
import sys
import traceback
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Sequence, Any, Union, Optional

import coloredlogs

import coveriteam
import coveriteam.util as util
from coveriteam.interpreter.python_code_generator import generate_python_code
from coveriteam.interpreter.utility_visitors import download_atomic_actors
from coveriteam.remote_client import exec_remotely


class CoVeriTeam:
    def start(self, argv):
        self.config = self.create_argument_parser().parse_args(argv)

        assert self.config.remote or (self.config.remote_url is None)

        str_to_prepend = ""

        logger_level = logging.WARNING
        if self.config.debug:
            logger_level = util.CVT_DEBUG_LEVEL

        if self.config.debug_deep:
            logger_level = logging.DEBUG

        FORMAT = "%(asctime)-15s %(levelname)s %(message)s"
        # Installs a handler for all logging levels from log_level upwards
        coloredlogs.install(level=logger_level, fmt=FORMAT)

        if self.config.cache_dir:
            util.set_cache_directories(Path(self.config.cache_dir).resolve())
        else:
            util.set_cache_directories()

        if self.config.no_cache_update:
            util.set_cache_update(False)
        else:
            util.set_cache_update(True)

        util.set_use_mpi_flag(self.config.portfolio_use_mpi)

        if self.config.clean:
            # Remove both the archive and unzip directory
            shutil.rmtree(util.INSTALL_DIR)
            shutil.rmtree(util.ARCHIVE_DOWNLOAD_PATH)
            shutil.rmtree(util.TOOL_INFO_DOWNLOAD_PATH)
            util.create_cache_directories()

        if self.config.testtool:
            from coveriteam.language.atomicactor import AtomicActor

            a = AtomicActor(self.config.input_file)
            a.print_version()
            return

        if self.config.gettool:
            from coveriteam.language.atomicactor import AtomicActor

            a = AtomicActor(self.config.input_file)
            return

        if self.config.inputs:
            str_to_prepend += (
                "\n".join([f"{k} = {repr(v)}" for k, v in self.config.inputs.items()])
                + "\n"
            )

            str_to_prepend += "from coveriteam.language.actor import Actor\n"

            trusted = (
                f'"{self.config.trust_tool_info}"'
                if self.config.trust_tool_info
                else "False"
            )
            str_to_prepend += "Actor.trust_tool_info = " + trusted + "\n"

            allow_cgroups = (
                f"{self.config.allow_cgroup_access_to_actors}"
                if self.config.allow_cgroup_access_to_actors
                else "False"
            )
            str_to_prepend += f"Actor.allow_cgroup_access = {allow_cgroups}\n"

        if self.config.input_file:
            if self.config.only_install_actors:
                download_atomic_actors(self.config.input_file)
                return

            if self.config.remote:
                exec_remotely(self.config)
                return
            """"CVL file is provided."""
            generated_code = str_to_prepend + generate_python_code(
                self.config.input_file
            )
            if self.config.generate_code:
                print(generated_code)
            else:
                try:
                    exec(generated_code, globals())  # noqa S102
                except NameError as e:
                    logging.error(str(e))  # noqa G200
                    logging.error("Maybe you forgot or mistyped an input")
                    if self.config.debug or self.config.debug_deep:
                        print(traceback.format_exc())

    def create_argument_parser(self):
        """
        Create a parser for the command-line options.
        @return: an argparse.ArgumentParser instance
        """
        parser = argparse.ArgumentParser(
            prog="coveriteam",
            fromfile_prefix_chars="@",
            description="""Execute a program written in CoVeriLang.
               Command-line parameters can additionally be read from a file if file name prefixed with '@' is given as argument.
               """,
        )
        parser.add_argument(
            "--version", action="version", version=f"{coveriteam.__version__}"
        )

        parser.add_argument(
            "--get-tool",
            dest="gettool",
            action="store_true",
            default=False,
            help="Download the tool archive and initialize an atomic actor for the given YML file configuration.",
        )

        parser.add_argument(
            "--only-install-actors",
            dest="only_install_actors",
            action="store_true",
            default=False,
            help="Downloads all atomic actors with the given version.",
        )

        parser.add_argument(
            "--tool-info",
            dest="testtool",
            action="store_true",
            default=False,
            help="Test the given YML file configuration by executing the tool for version.",
        )

        parser.add_argument(
            "input_file",
            metavar="INPUT_FILE",
            help="The program written in CoVeriLang or a YML configuration if testing a tool.",
        )
        parser.add_argument(
            "--input",
            action=InputAction,
            dest="inputs",
            help="Inputs to the CoVeriLang program provided in the form of key=val "
            "for unique keys and key+=val to append key value pair.",
        )

        parser.add_argument(
            "--gen-code",
            dest="generate_code",
            action="store_true",
            default=False,
            help="Flag to generate python code from the cvl file.",
        )

        parser.add_argument(
            "--clean",
            dest="clean",
            action="store_true",
            default=False,
            help="Clean the tmp directory, which contains the extracted archives of the atomic actors.",
        )

        parser.add_argument(
            "--debug",
            dest="debug",
            action="store_true",
            default=False,
            help="Set the logging to debug for CoVeriTeam. Only logs debug (and higher) messages from CoVeriTeam",
        )

        parser.add_argument(
            "--debug-deep",
            dest="debug_deep",
            action="store_true",
            default=False,
            help="Set the logging to debug globally. Also logs debug (and higher) messages from BenchExec.",
        )

        parser.add_argument(
            "--cache-dir", metavar="CACHE_DIR", help="Path to the cache."
        )

        parser.add_argument(
            "--remote",
            dest="remote",
            action="store_true",
            default=False,
            help="Execute CoVeriTeam remotely.",
        )

        parser.add_argument(
            "--remote-url", metavar="REMOTE_URL", help="URL to the web service."
        )

        parser.add_argument(
            "--verbose",
            dest="verbose",
            action="store_true",
            default=False,
            help="Flag to print verbose output. At the moment supported only for remote execution.",
        )

        parser.add_argument(
            "--trust-tool-info",
            dest="trust_tool_info",
            action="store_true",
            default=False,
            help="Trust the tool info modules. This will load them without a container.",
        )

        parser.add_argument(
            "--allow-cgroup-access-to-actors",
            dest="allow_cgroup_access_to_actors",
            action="store_true",
            default=False,
            help="Allow the access to c-groups for each atomic actor.",
        )

        parser.add_argument(
            "--no-cache-update",
            dest="no_cache_update",
            action="store_true",
            default=False,
            help="Do not update the cache. Only use tools available in the cache. If tools are not available, then CoVeriTeam simply fails.",
        )

        parser.add_argument(
            "--use-mpi-for-portfolio",
            dest="portfolio_use_mpi",
            action="store_true",
            default=False,
            help="Execute portfolio using python processes instead of using MPI (even if MPI is available). Relevant if executing portfolio using only one machine.",
        )
        return parser


class InputAction(argparse.Action):
    """Custom Action for the --input parameter

    This class defines a custom action for the --input parameter in the argparse.ArgumentParser
    Inputs can be given as key=value or key+=values pairs. For example:
        --input program=path/to/program.c
        --input program+=path/to/program.c
    When = is used as separator this action enforces the key to be unique in all inputs given with --input.

    When += is used this action will append the given key-value-pair to the current input list in the argparse.Namespace of the argparse.ArgumentParser
    """

    def __call__(
        self,
        parser: ArgumentParser,
        # Namespace, which will be returned from parse_args
        namespace: Namespace,
        # Value after --input
        values: Union[str, Sequence[Any], None],
        # Option which triggered this action, in our case --input
        option_string: Optional[str] = ...,
    ) -> None:
        if not values:
            raise ValueError("Empty --input argument")
        if isinstance(values, collections.abc.Sequence):
            values = "".join(values)

        append = True
        value_list = values.split("+=")
        if len(value_list) != 2:
            append = False
            value_list = values.split("=")
        if len(value_list) != 2:
            raise NameError("Invalid input %s" % values)

        key, value = value_list
        if not namespace.__getattribute__(self.dest):
            namespace.__setattr__(self.dest, {})

        inputs_list = namespace.__getattribute__(self.dest)

        if key in inputs_list:
            if append:
                entry = inputs_list[key]
                if isinstance(entry, list) and not isinstance(entry, str):
                    entry.append(value)
                else:
                    inputs_list[key] = [entry, value]
            else:
                raise ValueError("Key %s already specified in inputs" % key)
        else:
            inputs_list[key] = value


def main(argv=None):
    args = argv or sys.argv
    CoVeriTeam().start(args[1:])


if __name__ == "__main__":
    main()
