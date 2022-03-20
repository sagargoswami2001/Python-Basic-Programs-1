# Write a Python Program to sum of two given integers. However, if the sum is between 15 to 20.

def sum(x, y):
    sum = x + y
    if sum in range(15,20):
        return 20
    else:
        return sum

print(sum(10,6))
print(sum(10,2))
print(sum(10,12))