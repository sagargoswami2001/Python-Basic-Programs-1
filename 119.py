# Write a Python Program to get the Size of an Object in Bytes.
import sys
str1 = "one"
str2 = "Four"
str3 = "Three"
print()
print("Memory Size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " Bytes")
print("Memory Size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " Bytes")
print("Memory Size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " Bytes")
print()