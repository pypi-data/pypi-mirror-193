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


class LogUtils:
    @staticmethod
    def log(tag: str, message: str, *args: PrintCode):
        print(LogUtils.wrap(tag, message, *args))
        sys.stdout.flush()

    @staticmethod
    def i(tag: str, message: str):
        LogUtils.log(tag, message, PrintCode.GREEN)

    @staticmethod
    def d(tag: str, message: str):
        LogUtils.log(tag, message, PrintCode.CYAN, PrintCode.BOLD)

    @staticmethod
    def w(tag: str, message: str):
        LogUtils.log(tag, message, PrintCode.BOLD, PrintCode.YELLOW)

    @staticmethod
    def e(tag: str, message: str):
        LogUtils.log(tag, message, PrintCode.BOLD, PrintCode.RED)

    @staticmethod
    def wrap(tag: str, message: str, *args: PrintCode) -> str:
        mapped_value = map(lambda code: str(code.value), args)
        joined_str = ";".join(mapped_value)
        return f'\033[{joined_str}m{tag} >>> {message}\033[0m'
