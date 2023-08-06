# This file is part of CoVeriTeam, a tool for on-demand composition of cooperative verification systems:
# https://gitlab.com/sosy-lab/software/coveriteam
#
# SPDX-FileCopyrightText: 2020 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

import logging
import os
import shutil
import test_util  # noqa F401
import threading
import time
from pathlib import Path

import pytest

import coveriteam.util
import tests

from coveriteam.coveriteam import CoVeriTeam
from coveriteam.language.parallel_portfolio import ParallelPortfolio
from coveriteam.language.actor import Actor
from coveriteam.language import artifact
from coveriteam.language.atomicactor import AtomicActor, ExecutionState

cpa_seq: AtomicActor = None
uautomizer: AtomicActor = None
legion: AtomicActor = None
symbiotic: AtomicActor = None
esbmc_kind: AtomicActor = None

short_c_program: artifact.CProgram = None
heavy_c_program: artifact.CProgram = None

spec_unreached_call: artifact.Specification = None

example_dir_path: Path = None


def setup_module():
    global cpa_seq, uautomizer, legion, symbiotic, esbmc_kind
    global short_c_program, spec_unreached_call, heavy_c_program
    global example_dir_path

    coveriteam.util.set_cache_directories()
    coveriteam.util.set_cache_update(True)

    cpa_seq = tests.ProgramVerifier("actors/cpa-seq.yml")
    uautomizer = tests.ProgramVerifier("actors/uautomizer.yml")
    legion = tests.ProgramVerifier("actors/legion.yml")
    symbiotic = tests.ProgramVerifier("actors/symbiotic.yml")
    esbmc_kind = tests.ProgramVerifier("actors/esbmc-kind.yml")

    short_c_program = artifact.CProgram(tests.TEST_DATA_DIR + "c/error.i")
    heavy_c_program = artifact.CProgram(
        tests.TEST_DATA_DIR + "c/sanfoundry_43_ground.i"
    )

    spec_unreached_call = artifact.BehaviorSpecification(
        tests.property_path_reach_safety
    )

    logging_format = "%(asctime)-15s %(levelname)s %(message)s"
    logging.basicConfig(level=logging.WARNING, format=logging_format)
    example_dir_path = Path(os.getcwd()) / "examples"


def teardown_module():
    if os.getcwd().endswith("examples"):
        shutil.rmtree("./cvt-output")
        os.chdir("..")

    if os.getcwd().endswith("coveriteam"):
        shutil.rmtree("./cvt-output", ignore_errors=True)
        last = Path("lastexecution")
        if last.is_symlink() or last.exists():
            last.unlink()


def timing(f):
    def wrap(*args):
        time1 = time.time()
        try:
            ret = f(*args)
        except Exception:
            ret = None
        time2 = time.time()
        print("%s function took %0.3f s" % ("Test", (time2 - time1)))
        return ret

    return wrap


def test_portfolio_cvt():
    test_cvt_file("portfolio.cvt")


def test_portfolio_in_portfolio_cvt():
    test_cvt_file("portfolio-in-portfolio.cvt")


def test_portfolio_tester_cvt():
    args = {
        "program_path": str(example_dir_path / "test-data/c/test1.c"),
        "specification_path": str(
            example_dir_path / "test-data/properties/coverage-error-call.prp"
        ),
    }

    test_cvt_file("portfolio-tester.cvt", args)


def test_validating_portfolio_cvt():
    test_cvt_file("validating-portfolio.cvt")


@pytest.mark.skip()
def test_cvt_file(cvt_file_name: str, input_args: dict = None):
    if not input_args:
        input_args = {
            "program_path": str(example_dir_path / "test-data/c/error.i"),
            "specification_path": str(
                example_dir_path / "test-data/properties/unreach-call.prp"
            ),
            "data_model": "ILP32",
        }

    inputs = [str(example_dir_path / cvt_file_name)]
    for k, v in input_args.items():
        inputs += ["--input", f"{k}={v}"]

    CoVeriTeam().start(inputs)


def test_mpi_basic_test():
    test_basic_execution()


@pytest.mark.skip()
def test_basic_multiprocessing_processes_execution():
    test_basic_execution(True)


@pytest.mark.skip()
def test_portfolio_with_multiprocessing_mpi_execution():
    test_portfolio_in_portfolio()


@pytest.mark.skip()
def test_portfolio_with_multiprocessing_processes_execution():
    test_portfolio_in_portfolio(True)


@pytest.mark.skip(reason="currently failing")
def test_await_all_processes():
    test_wait_all_actor_execution(True)
    test_wait_all_actor_execution()


@pytest.mark.skip()
def test_termination():
    test_termination_of_portfolio(True)
    test_termination_of_portfolio()


@pytest.mark.skip()
def test_atomic_actor_shutdown():
    test_atomic_actor_stop_procedure(True)
    test_atomic_actor_stop_procedure()


@pytest.mark.skip()
def test_basic_execution(use_multiprocessing_processes=False):
    Actor.trust_tool_info = False
    coveriteam.util.PORTFOLIO_USE_MPI = use_multiprocessing_processes

    assert uautomizer.execution_state is not ExecutionState.Stopping

    res = ParallelPortfolio(
        [
            cpa_seq,
            uautomizer,
            esbmc_kind,
        ]
    ).act(program=short_c_program, spec=spec_unreached_call)

    assert res["verdict"] == "false"


@pytest.mark.skip()
def test_portfolio_in_portfolio(use_multiprocessing_processes=False):
    Actor.trust_tool_info = False
    coveriteam.util.PORTFOLIO_USE_MPI = use_multiprocessing_processes

    res = ParallelPortfolio(
        [
            symbiotic,
            uautomizer,
            ParallelPortfolio([cpa_seq, symbiotic]),
        ]
    ).act(program=short_c_program, spec=spec_unreached_call)
    print(res)
    assert res["verdict"] == "false"


@pytest.mark.skip()
def test_atomic_actor_stop_procedure(use_mpi=False):
    Actor.trust_tool_info = False
    coveriteam.util.PORTFOLIO_USE_MPI = use_mpi

    # Actor verifier-false produces no witness
    # The results of this actor is always VERDICT_DISCARDED(NO WITNESS)
    dummy_actor = tests.ProgramVerifier("actors/verifier-false.yml")
    portfolio = ParallelPortfolio(
        [uautomizer, dummy_actor],
        success_condition='verdict in ["VERDICT_DISCARDED(NO WITNESS)", RESULT_CLASS_TRUE, RESULT_CLASS_FALSE]',
    )

    # UAutomizer takes a lot of cpu time to check this program
    uautomizer_heavy_program = artifact.CProgram(
        tests.TEST_DATA_DIR + "c/CostasArray-10.c"
    )

    start = time.perf_counter()
    portfolio.act(program=uautomizer_heavy_program, spec=spec_unreached_call)
    finished_time = time.perf_counter() - start

    # tested on local machine, needed 4 secs with MPI and 1.4 with Python processes for shutdown
    # The task chosen fpr this test uses somewhat 30+ secs on the used local machine, CI would need much more
    time_limit_for_shutdown = 12 if use_mpi else 4

    print(f"{'MPI' if use_mpi else 'Python'}: Shutdown took {finished_time}s time")
    assert finished_time < time_limit_for_shutdown


def heavy_load():
    for _i in range(10):
        ParallelPortfolio.use_multiprocessing = (
            not ParallelPortfolio.use_multiprocessing
        )
        test_portfolio_cvt()


@pytest.mark.skip()
def test_wait_all_actor_execution(use_multiprocessing_processes=False):
    Actor.trust_tool_info = False
    coveriteam.util.PORTFOLIO_USE_MPI = use_multiprocessing_processes

    res = ParallelPortfolio([uautomizer, uautomizer, uautomizer, uautomizer]).act(
        program=short_c_program, spec=spec_unreached_call
    )
    print(res)


@pytest.mark.skip()
def test_termination_of_portfolio(use_multiprocessing_processes=False):
    Actor.trust_tool_info = False
    coveriteam.util.PORTFOLIO_USE_MPI = use_multiprocessing_processes

    portfolio = ParallelPortfolio(
        [
            cpa_seq,
            esbmc_kind,
            symbiotic,
        ]
    )

    def terminate_after_time():
        # Timer must be high enough so that the actors are started
        time.sleep(8)
        portfolio.stop()

    threading.Thread(target=terminate_after_time).start()
    try:
        res = portfolio.act(program=heavy_c_program, spec=spec_unreached_call)
        print(res)
    except AttributeError as e:
        # Workaround, because dummy result creation isn't working properly
        print(e)
        assert str(e) == "'Verdict' object has no attribute 'items'"
