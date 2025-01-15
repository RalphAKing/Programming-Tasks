# Logging Decorator Challenge

## Objective
Create a decorator that logs function calls, including their arguments and return values.

## Requirements
1. The decorator should work with functions that have:
   - Positional arguments
   - Keyword arguments
   - A mix of both (*args and **kwargs)
2. Log the function name, arguments, and return value in a readable format.

## Example Usage

```python
@logged
def add_numbers(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

result = add_numbers(1, 2, 3, a=4, b=5)
```

## Expected Output

Basic
```
Function 'add_numbers' called with args=(1, 2, 3) and kwargs={'a': 4, 'b': 5}
Function 'add_numbers' returned: 15
```

## Bonus Challenges
1. Add a timestamp to each log entry.
2. Allow the user to specify the logging level (e.g., INFO, DEBUG, ERROR).
3. Implement pretty-printing for complex return values (e.g., nested dictionaries or lists).
4. Provide an option to log to a file instead of just printing to console.
5. Handle and log exceptions if they occur during function execution.

## Evaluation Criteria
- Correctness: Does the decorator work as expected?
- Readability: Is the code clean and well-commented?
- Flexibility: Can it handle various function signatures?
- Error Handling: Does it gracefully handle and log exceptions?
