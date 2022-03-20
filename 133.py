# Write a Python Program to Check Whether a String is Numeric.

str = 'a123'

try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot Numeric')
print()