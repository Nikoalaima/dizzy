# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: SalesPipeline
import os
import sys

ANSI = sys.stderr.isatty()

def _c(f):
    return f if ANSI else lambda *a, **k: None

class B:
    RESET = _c("\033[0m")
    RED = _c("\033[31m")
    GREEN = _c("\033[32m")
    YELLOW = _c("\033[33m")
    BLUE = _c("\033[34m")
    MAGENTA = _c("\033[35m")
    CYAN = _c("\033[36m")
    WHITE = _c("\033[37m")
    BG_RED = _c("\033[41m")
    BG_GREEN = _c("\033[42m")
    BG_YELLOW = _c("\033[43m")
    BOLD = _c("\033[1m")

def _info(msg):
    print(B.BLUE + B.BOLD + msg + B.RESET)

def _warn(msg):
    print(B.YELLOW + msg + B.RESET)

def _success(msg):
    print(B.GREEN + msg + B.RESET)

def _error(msg):
    print(B.RED + msg + B.RESET)

def _debug(msg):
    if os.environ.get("SALES_DEBUG"):
        print(B.MAGENTA + "[DEBUG]" + msg + B.RESET)
