# Write a Python Program Check whether Triangle is valid or not if sides are given.

def checkValidity(a, b, c):

    # check condition
    if (a + b < c) or (a + c < b) or (b + c < a):
        return False
    else:
        return True

# Driver Code
a = 7
b = 10
c = 5

if checkValidity(a, b, c):
    print("Valid")
else:
    print("Invalid")