# Write a Program to Print Multiplication Table of a Given Number Using For Loop.

num = int(input("Enter the Number: "))
for i in range(1,11):
   # print(str(num) + " X " + str(i) + " = " + str(num*i))
    print(f"{num} X {i} = {num*i}")