# Write a Python Program to Calculate the Sum of the Digits in an Integer.

num = int(input("Input a Four Digit Numbers: "))
x = num // 1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The Sum of Digits in the Number is", x+x1+x2+x3)