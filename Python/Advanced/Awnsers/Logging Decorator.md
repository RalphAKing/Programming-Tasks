# Logging Decorator Challenge Solution

## Basic Solutions

### Class
```python
class LoggingDecorator:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # Log function call
            print(f"Function '{func.__name__}' called with args={args} and kwargs={kwargs}")

            # Execute the function
            result = func(*args, **kwargs)

            # Log function return
            print(f"Function '{func.__name__}' returned: {result}")

            return result
        return wrapper

# Usage
logged = LoggingDecorator()

@logged
def add_numbers(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

# Test the decorator
result = add_numbers(1, 2, 3, a=4, b=5)
print(f"Result: {result}")
```

### Function
```python
def logged(func):
    def wrapper(*args, **kwargs):
        # Log function call
        print(f"Function '{func.__name__}' called with args={args} and kwargs={kwargs}")

        # Execute the function
        result = func(*args, **kwargs)

        # Log function return
        print(f"Function '{func.__name__}' returned: {result}")

        return result
    return wrapper

@logged
def add_numbers(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

# Test the decorator
result = add_numbers(1, 2, 3, a=4, b=5)
print(f"Result: {result}")
```

### Functools
```python
import functools

def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log function call
        print(f"Function '{func.__name__}' called with args={args} and kwargs={kwargs}")

        # Execute the function
        result = func(*args, **kwargs)

        # Log function return
        print(f"Function '{func.__name__}' returned: {result}")

        return result
    return wrapper

@logged
def add_numbers(*args, **kwargs):
    """Add numbers together."""
    return sum(args) + sum(kwargs.values())

# Test the decorator
result = add_numbers(1, 2, 3, a=4, b=5)
print(f"Result: {result}")

# Demonstrate that function metadata is preserved
print(f"Function name: {add_numbers.__name__}")
print(f"Function docstring: {add_numbers.__doc__}")
```

## Bonus Solutions

### Class
```python

```