# Write a Python Program that Accepts an Interger (n) and Computes the Value of n+nn+nnn.
a = int(input("Input an Integer: "))
n1 = int("%s" %a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1+n2+n3)