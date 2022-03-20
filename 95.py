# Write a Program to find the Sum of First n Natural Numbers Using While Loop.

num = int(input("Enter the Number: "))
if num < 0:
    print("Enter a Positive Number: ")
else:
    sum = 0

# Use While Loop to Iterate Until Zero.
while(num > 0):
    sum += num
    num -= 1
print("The Result is", sum)