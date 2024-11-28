def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")  # Raise an exception if b is zero
    return a / b

try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)  # Handle the exception with an except block