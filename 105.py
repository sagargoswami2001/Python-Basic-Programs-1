# Find Average of N Numbers in Python.

num = int(input("How Many Number: "))
total_sum = 0

for s in range(num):
    numbers = float(input("Enter Number: "))
    total_sum += numbers

avg = total_sum / num
print("Average is: ", avg)