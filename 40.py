'''
Write a Python Program to find whether a given number (accept from the user) is even or odd,
print out an appropriate message to the user.
'''
num = int(input("Enter a Number: "))
mod = num % 2
if mod > 0:
    print("This is an Odd Number.")
else:
    print("This is an Even Number.")
    