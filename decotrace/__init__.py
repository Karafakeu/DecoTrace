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