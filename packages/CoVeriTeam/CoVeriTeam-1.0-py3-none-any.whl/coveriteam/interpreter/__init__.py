# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0
import logging
import sys

from antlr4 import FileStream, CommonTokenStream

from coveriteam.parser.CoVeriLangLexer import CoVeriLangLexer
from coveriteam.parser.CoVeriLangParser import CoVeriLangParser


def get_parsed_tree(path):
    try:
        input_stream = FileStream(path, encoding="utf-8")
    except FileNotFoundError as e:
        logging.error("Can not find file %s", e.filename)
        sys.exit("Exiting CoVeriTeam...........")

    lexer = CoVeriLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CoVeriLangParser(token_stream)
    return parser.program()
