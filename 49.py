'''Write a Python Program to Compute the Greatest Common Divisor (GCD) of two positive Integers.'''

def gcd(x,y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
        return gcd

print(gcd(12, 17))
print(gcd(4, 7))