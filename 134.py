# Write a Python Program to Print the Current Call Stack.

import traceback
print()
def f1():return abc()
def abc():traceback.print_stack()
f1()
print()