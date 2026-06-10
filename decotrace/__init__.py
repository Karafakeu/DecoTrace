import sys
import linecache
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("decotrace-debug")
except PackageNotFoundError:
    __version__ = "unknown"


def decotrace(func):
    def wrapper(*args, **kwargs):
        print(f"Starting DecoTrace {__version__} -> {func.__name__}()")
        result = func(*args, **kwargs)
        print("Stopping DecoTrace")
        return result
    return wrapper
