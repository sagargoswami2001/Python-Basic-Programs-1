# Write a Program to Print Multiplication Table of N Using for Loop in Reversed Order.

num = int(input("Enter the Number: "))
for i in range(10,0,-1):
   # print(str(num) + " X " + str(i) + " = " + str(num*i))
    print(f"{num} X {i} = {num*i}")