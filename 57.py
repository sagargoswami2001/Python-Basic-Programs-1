# Write a Python Program to Compute the Future Value of a Specified Principle Amount, rate of interest, and a Number of Years.

amt = 10000
int = 3.5
Years = 7

future_value = amt*((1+(0.01*int)) ** Years)
print(round(future_value,2))