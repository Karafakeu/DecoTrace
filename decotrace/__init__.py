import functools

__version__ = "1.0.0"


def decotrace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting DecoTrace {__version__}")
        result = func(*args, **kwargs)
        print("Stopping DecoTrace")
        return result
    return wrapper
