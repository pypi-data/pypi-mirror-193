"""
A logger that gets dumped to stdout when closed
"""

import inspect
import itertools
import logging
import os

from logging.handlers import MemoryHandler
from typing import Any, Optional


class MemoryLogger:
    """
    A logger that gets dumped to stdout when closed
    """

    id_iter = itertools.count()

    def __init__(  # pylint: disable=too-many-arguments
        self,
        file_name: str,
        lock: Optional[Any],
        log_name: Optional[str] = None,
        log_level: int = logging.INFO,
        flush_immed: bool = False,
    ) -> None:
        self.instance_id = next(self.id_iter)
        self.flush_immed = flush_immed
        self.lock = lock

        if log_name is None:
            caller = inspect.stack()[1][0].f_locals["self"].__class__.__name__
            log_name = f"{caller}--{os.getpid()}-{self.instance_id}"

        self._logger = logging.getLogger(log_name)

        self._logger.setLevel(log_level)

        fmt = " - ".join(
            [
                "[$asctime]",
                "[$name]",
                "[$levelname]",
                "$message",
            ]
        )

        formatter = logging.Formatter(
            fmt=fmt,
            style="$",
        )

        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)

        log_handler = MemoryHandler(10000, flushLevel=logging.CRITICAL, target=file_handler)

        log_handler.setFormatter(formatter)
        self._logger.addHandler(log_handler)

    def flush(self) -> None:
        """
        Flush all handlers for this logger
        """
        if self.lock is not None:
            with self.lock:
                for handler in self._logger.handlers:
                    handler.flush()
        else:
            for handler in self._logger.handlers:
                handler.flush()

    def close(self) -> None:
        """
        Close (and flush) all handlers for this logger
        """
        if self.lock is not None:
            with self.lock:
                for handler in self._logger.handlers:
                    handler.close()
        else:
            for handler in self._logger.handlers:
                handler.close()

    def clear_targets(self) -> None:
        """
        Makes the target for all Memory Handlers in this logger None

        Thus when these handlers are flushed, nothing will go to standard output
        """
        for handler in self._logger.handlers:
            if isinstance(handler, MemoryHandler):
                handler.setTarget(None)

    def log(self, level: int, msg: str, indent_level: int) -> None:
        """
        Wrapper function for logging messages
        """
        indent_string = " " * 4 * indent_level

        self._logger.log(level, indent_string + msg)
        if self.flush_immed:
            self.flush()

    def debug(self, msg: str, indent_level: int = 0) -> None:
        """
        Wrapper function for debug messages
        """
        self.log(logging.DEBUG, msg, indent_level)

    def info(self, msg: str, indent_level: int = 0) -> None:
        """
        Wrapper function for info messages
        """
        self.log(logging.INFO, msg, indent_level)

    def warning(self, msg: str, indent_level: int = 0) -> None:
        """
        Wrapper function for warn messages
        """
        self.log(logging.WARNING, msg, indent_level)

    def error(self, msg: str, indent_level: int = 0) -> None:
        """
        Wrapper function for error messages
        """
        self.log(logging.ERROR, msg, indent_level)

    def fatal(self, msg: str, indent_level: int = 0) -> None:
        """
        Wrapper function for fatal messages
        """
        self.log(logging.FATAL, msg, indent_level)

    def critical(self, msg: str, indent_level: int = 0) -> None:
        """
        Wrapper function for critical messages
        """
        self.log(logging.CRITICAL, msg, indent_level)
