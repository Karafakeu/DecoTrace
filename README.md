# DecoTrace

A lightweight Python debugging library built on decorators.

## Overview

DecoTrace provides a simple, non-intrusive way to debug Python functions. Instead of scattering print statements throughout your code or reaching for a full IDE debugger, you can attach a single decorator to any function and get immediate insight into its execution.

## Usage

Apply `@decotrace` to any function you want to debug:

```python
from decotrace import decotrace

@decotrace
def my_function(x, y):
    return x + y
```

To customize the debugging behavior, pass options to the decorator:

```python
@decotrace(verbose=True)
def my_function(x, y):
    return x + y
```

## Options

| Option | Type | Description |
|--------|------|-------------|
| `verbose` | `bool` | Enables detailed output during function execution |
| `variables` | `bool` | Displays variable state during function execution |

## Philosophy

DecoTrace is designed to stay out of your way. Add it when you need it, remove it when you don't. No configuration files, no project-wide setup — just a decorator.
