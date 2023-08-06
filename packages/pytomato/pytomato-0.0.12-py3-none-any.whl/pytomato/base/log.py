# encoding:utf-8
import sys
from enum import Enum

__all__ = ['PrintCode', 'LogUtils']


class PrintCode(Enum):
    # text style
    BOLD = 1
    ITALIC = 3
    UNDERLINE = 4
    # text color
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    GREY = 37
    # background color
    BG_BLACK = 40
    BG_RED = 41
    BG_GREEN = 42
    BG_YELLOW = 43
    BG_BLUE = 44
    BG_MAGENTA = 45
    BG_CYAN = 46
    BG_GREY = 47


class LogLevel:
    verbose = 0
    info = 1
    debug = 2
    warning = 3
    error = 4


class LogUtils:
    _log_level = LogLevel.verbose

    @classmethod
    def set_log_level(cls, level: int):
        cls._log_level = level

    @classmethod
    def _log(cls, level: int, tag: str, message: str, *args: PrintCode):
        if cls._log_level > level:
            return
        print(cls._wrap(tag, message, *args))
        sys.stdout.flush()

    @classmethod
    def i(cls, tag: str, message: str):
        cls._log(LogLevel.info, tag, message, PrintCode.GREEN)

    @classmethod
    def d(cls, tag: str, message: str):
        cls._log(LogLevel.debug, tag, message, PrintCode.CYAN, PrintCode.BOLD)

    @classmethod
    def w(cls, tag: str, message: str):
        cls._log(LogLevel.warning, tag, message, PrintCode.BOLD, PrintCode.YELLOW)

    @classmethod
    def e(cls, tag: str, message: str):
        cls._log(LogLevel.error, tag, message, PrintCode.BOLD, PrintCode.RED)

    @classmethod
    def _wrap(cls, tag: str, message: str, *args: PrintCode) -> str:
        mapped_value = map(lambda code: str(code.value), args)
        joined_str = ";".join(mapped_value)
        return f'\033[{joined_str}m{tag} >>> {message}\033[0m'
