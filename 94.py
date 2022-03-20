# Write a Program to find Whether a Given Number is Prime or Not.

num = int(input("Enter the Number: "))
prime = True
for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This Number is Prime")
else:
    print("This Number is Not Prime")