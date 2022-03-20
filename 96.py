# Write a Program to Calculate the Factorial of a Given Number Using For Loop.
# n! = 1 X 2 X 3 X ..... Xn

num = int(input("Enter the Number: "))
factorial = 1
for a in range(1, num+1):
    factorial = factorial * a
print(f"The Factorial of {num} is {factorial}")