# Copyright (c) 2022, INRIA
# Copyright (c) 2022, University of Lille
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
Launch the whole architecture, crash the formula with a fatal error and test if the whole architecture is interupted

Architecture :
  - 1 puller (connected to MongoDB1 [collection test_hwrep], stream mode on)
  - 1 dispatcher (HWPC dispatch rule (dispatch by ROOT)
  - 1 Dummy Formula
  - 1 pusher (connected to MongoDB1 [collection test_result]

MongoDB1 content:
  - 1 HWPC Report

Test if:
  - if the architecture process was terminated
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
# pylint: disable=unused-import
import logging
import sys
import time
import signal
import os

from multiprocessing import Process

import pytest

from powerapi.actor import Supervisor
from powerapi.handler import Handler
from powerapi.message import PoisonPillMessage
from powerapi.report import PowerReport, Report
from powerapi.test_utils.db.mongo import mongo_database
from powerapi.test_utils.acceptation import mongodb_content, MainProcess
from powerapi.formula import FormulaState, AbstractCpuDramFormula, FormulaActor, \
    FormulaPoisonPillMessageHandler

from powerapi.test_utils.acceptation import BASIC_CONFIG, ROOT_DEPTH_LEVEL, launch_simple_architecture
from powerapi.test_utils.report.hwpc import extract_rapl_reports_with_2_sockets


#################
# Crash Formula #
#################
class CrashState(FormulaState):
    """
        State for a CrashFormulaActor
    """

    def __init__(self, actor, pushers, metadata, nb_reports_max, exception, sleep_time):
        FormulaState.__init__(self, actor, pushers, metadata)
        self.nb_reports = 0
        self.nb_reports_max = nb_reports_max
        self.exception = exception
        self.sleep_time = sleep_time

    def reinit(self):
        self.nb_reports = 0


class CrashException(Exception):
    """
        Exception to indicate that there is a crash
    """


class ReportHandler(Handler):
    """
        Handler for Reports in a CrashFormulaActor
    """

    def _estimate(self, report):
        if self.state.nb_reports >= self.state.nb_reports_max:
            raise self.state.exception()

        self.state.nb_reports += 1
        metadata = {'formula_name': self.state.actor.name}

        socket_id = self.state.metadata['socket'] if 'socket' in self.state.metadata else -1

        metadata['socket'] = socket_id

        result_msg = PowerReport(timestamp=report.timestamp, sensor=report.sensor, target=report.target, power=42,
                                 metadata=metadata)
        return [result_msg]

    def handle(self, msg):
        results = self._estimate(msg)
        for _, actor_pusher in self.state.pushers.items():
            for result in results:
                actor_pusher.send_data(result)


class CrashFormulaActor(AbstractCpuDramFormula):
    """
        Formula Actor that crash after a given number of reports are processed
    """

    def __init__(self, name, pushers, socket, core, nb_reports_max=5, exception=CrashException,
                 level_logger=logging.WARNING, sleep_time=0, timeout=None):
        AbstractCpuDramFormula.__init__(self, name, pushers, socket, core, level_logger, timeout)
        self.state = CrashState(self, pushers=pushers, metadata=self.formula_metadata,
                                nb_reports_max=nb_reports_max, exception=exception,
                                sleep_time=sleep_time)
        self.low_exception = [CrashException]

    def setup(self):
        FormulaActor.setup(self)
        self.add_handler(PoisonPillMessage, FormulaPoisonPillMessageHandler(self.state))
        self.add_handler(Report, ReportHandler(self.state))


@pytest.fixture
def main_process():
    """
        Return the process to be used for testing.
        At the end of the test, the process will be stopped
    """
    p = MainProcessTestCrashFormula()
    p.start()
    time.sleep(1)
    yield p
    try:
        os.kill(p.pid, signal.SIGTERM)
    except Exception:
        pass


class MainProcessTestCrashFormula(MainProcess):
    """
    Process that run the global architecture and crash the formula
    """

    def __init__(self):
        MainProcess.__init__(self, name='test_crash_dispatcher', sleep_time=0.5, formula_class=CrashFormulaActor)

    def run(self):
        MainProcess.run(self)
        self.supervisor.join()


def test_crash_formula(mongo_database, main_process):
    """
        Check that the actor system is actually stopped when the formula crashes
    """
    if main_process.is_alive():
        os.kill(main_process.pid, signal.SIGTERM)
        main_process.join(5)
        assert not main_process.is_alive()
    assert True
