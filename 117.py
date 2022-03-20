# Write a Python Program to test Whether the System is a Big-Endian Platform or Little-Endian Platform.
import sys
print()
if sys.byteorder == "Big":
    # intel, alpha
    print("Little-Endian Platform.")
else:
    # motorola, sparc
    print("Big-Endian Platform.")
print()