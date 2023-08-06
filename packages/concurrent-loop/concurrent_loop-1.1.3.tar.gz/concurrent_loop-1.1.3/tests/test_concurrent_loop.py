#      Concurrent: helper for running functions in a concurrent loop.
#      Copyright (C) 2022  KC Lee  lathe-rebuke.0c@icloud.com
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
import pytest
from time import sleep

from src.concurrent_loop.loops import ThreadLoop, ProcessLoop
from helper import (Incrementer, IncrementerWithException,
                    TestIncrementerException)


class TestInitialisation:
    """
    Test that ThreadLoop, ProcessLoop can be initialised with loop periodicity.
    """
    def test_thread_loop(self):
        th_loop = ThreadLoop(100)
        assert th_loop.period_ms == 100

    def test_process_loop(self):
        pr_loop = ProcessLoop(100)
        assert pr_loop.period_ms == 100


class TestStartStop:
    """
    Test that the thread/process starts and stops as expected, and functions.
    """
    @classmethod
    def loop_start_stop(cls, looper):
        incrementer = Incrementer(looper)
        assert looper.thread_process is None
        incrementer.concurrent_start()
        assert looper.thread_process.is_alive()
        orig_value = incrementer.counter
        sleep(0.3)
        assert incrementer.counter > orig_value
        incrementer.concurrent_stop()
        assert looper.thread_process is None

    def test_thread_loop(self):
        self.loop_start_stop(ThreadLoop(10))

    def test_process_loop(self):
        self.loop_start_stop(ProcessLoop(10))


class TestLoopSpeed:
    """
    Tests that the loop speed setting work.
    """
    @classmethod
    def loop_start_stop(cls, loop_type):
        slow_increment = Incrementer(loop_type(20))
        fast_increment = Incrementer(loop_type(10))

        slow_increment.concurrent_start()
        fast_increment.concurrent_start()
        orig_slow = slow_increment.counter
        orig_fast = fast_increment.counter
        sleep(0.3)
        dt_slow = slow_increment.counter - orig_slow
        dt_fast = fast_increment.counter - orig_fast
        slow_increment.concurrent_stop()
        fast_increment.concurrent_stop()

        assert dt_fast > 1.8*dt_slow
        assert dt_fast < 2.2*dt_slow

    def test_thread_loop(self):
        self.loop_start_stop(ThreadLoop)

    def test_process_loop(self):
        self.loop_start_stop(ProcessLoop)


class TestMultiInstanceIndependence:
    """
    Tests that stop command sent to one of many instances stops the expected
    one.
    """
    @classmethod
    def multi_loop_stop(cls, loop_type):
        num_of_inst = 5
        loopers = []
        incrementers = []
        for _ in range(num_of_inst):
            looper = loop_type(10)
            loopers.append(looper)
            incrementers.append(Incrementer(looper))
        for incrementer in incrementers:
            incrementer.concurrent_start()
        for looper in loopers:
            assert looper.thread_process.is_alive()
        for incr_iter in range(num_of_inst):
            incrementers[incr_iter].concurrent_stop()
            for loop_iter in range(num_of_inst):
                if loop_iter <= incr_iter:
                    assert loopers[loop_iter].thread_process is None
                else:
                    assert loopers[loop_iter].thread_process.is_alive()

    def test_thread_loop(self):
        self.multi_loop_stop(ThreadLoop)

    def test_process_loop(self):
        self.multi_loop_stop(ProcessLoop)


class TestExceptionRaise:
    """
    Tests that ThreadLoop.exception and ProcessLoop.exception properties
    start off with None before the concurrent loop starts, continues to be
    None once it starts, until an exception is raised in the underlying
    concurrent function.
    """
    @classmethod
    def loop_start_stop(cls, loop_type):
        incrementer = IncrementerWithException(loop_type(1))
        assert incrementer.exception is None
        incrementer.concurrent_start()
        assert incrementer.exception is None
        sleep(0.3)  # Excessive sleep time since it takes a while for a
        # ProcessLoop to start running.
        assert isinstance(incrementer.exception, TestIncrementerException)
        # Read once more to ensure the exception property is persistent
        assert isinstance(incrementer.exception, TestIncrementerException)

    def test_thread_loop(self):
        self.loop_start_stop(ThreadLoop)

    def test_process_loop(self):
        self.loop_start_stop(ProcessLoop)

