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
"""
Controls concurrent tasks, by threads or multiprocess.
"""
import logging
import multiprocessing
import queue
from threading import Thread

from concurrent_loop.base import LoopBase

# Set up logging
logging.basicConfig(level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class ThreadLoop(LoopBase):
    """
    Creates a thread to run in loops
    """
    _queue_type = queue.Queue
    _thread_process_type = Thread


class ProcessLoop(LoopBase):
    """
    Creates a thread to run in loops
    """
    _queue_type = multiprocessing.JoinableQueue
    _thread_process_type = multiprocessing.Process
