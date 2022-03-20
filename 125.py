# Write a Python Program to Check Whather a File Path is a File or a Directory.

import os
path = "abc.txt"
if os.path.isdir(path):
    print("\nIt is a Directory")
elif os.path.isdir(path):
    print("\nIt is a Normal File")
else:
    print("It is a Special File (Socket, FIFO, Device File)" )
print()