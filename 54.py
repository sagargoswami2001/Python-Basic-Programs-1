# Write a Python Program to add two objects if both objects are an integer type.

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 20))