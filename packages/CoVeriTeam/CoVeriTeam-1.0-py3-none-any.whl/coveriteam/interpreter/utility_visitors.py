# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

# Generated from CoVeriLang.g4 by ANTLR 4.7.2

from pathlib import Path

from coveriteam.interpreter import get_parsed_tree
from coveriteam.interpreter.python_code_generator import COVERITEAM_IMPORTS
from coveriteam.language.actorconfig import ActorConfig
from coveriteam.parser.CoVeriLangParser import CoVeriLangParser
from coveriteam.parser.CoVeriLangVisitor import CoVeriLangVisitor


class AtomicActorVisitor(CoVeriLangVisitor):
    """Only resolves atomic actors.

    Creates ActorConfigs to download these actors.
    """

    def __init__(self, path):
        # I need the cvt path to resolve the file paths.
        self.__cvt_path = Path(path).parent.resolve()

        # Importing everything from CoVeriTeam
        exec(COVERITEAM_IMPORTS, globals())  # noqa S102
        super().__init__()

    def visitAtomic(self, ctx: CoVeriLangParser.AtomicContext):
        actordef = ctx.name.text
        if ctx.name.type == CoVeriLangParser.STRING:
            actordef = str((self.__cvt_path / actordef.strip('"')).resolve())

        version = ""
        if ctx.version:
            # Sanitizing the version from surrounding " and '
            version = ctx.version.text.strip("'").strip('"')

        # Download of the atomic actor
        ActorConfig(actordef, version)


def download_atomic_actors(path_str):
    tree = get_parsed_tree(path_str)
    AtomicActorVisitor(path_str).visit(tree)


def remove_quotes(s):
    return s[1:-1]


# This class defines a complete listener for a parse tree produced by CoVeriLangParser.
class FileCollector(CoVeriLangVisitor):
    files = []

    def __init__(self, path):
        # TODO don't know a better way to do it.
        # I need the cvt path to resolve the file paths.
        self.__cvt_path = Path(path).parent.resolve()
        super().__init__()

    # Visit a parse tree produced by CoVeriLangParser#spec_stmt.
    def visitSpec_stmt(self, ctx: CoVeriLangParser.Spec_stmtContext):
        a = ctx.assignable()
        if a.STRING():
            self.files += [remove_quotes(a.STRING().getText())]
        else:
            self.visitAssignable(a)

    # Visit a parse tree produced by CoVeriLangParser#Atomic.
    def visitAtomic(self, ctx: CoVeriLangParser.AtomicContext):
        if ctx.STRING():
            actordef = remove_quotes(ctx.STRING().getText())
            self.files += [actordef]

    # Visit a parse tree produced by CoVeriLangParser#artifact.
    def visitArtifact(self, ctx: CoVeriLangParser.ArtifactContext):
        if ctx.STRING():
            path = remove_quotes(ctx.STRING().getText())
            self.files += [path]


def collect_files(path_str):
    tree = get_parsed_tree(path_str)

    visitor = FileCollector(path_str)
    visitor.visit(tree)
    return visitor.files
