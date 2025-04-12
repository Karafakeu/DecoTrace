import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function {func.__name__} took {(end - start):.2f} seconds')
        return result
    return wrapper

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} was called')
        return func(*args, **kwargs)
    return wrapper

def trace_args(func):
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} was called with {args} and {kwargs}')
        return func(*args, **kwargs)
    return wrapper