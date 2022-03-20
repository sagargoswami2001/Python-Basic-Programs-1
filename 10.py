# Write a Python Program to Accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The Extension of the file is: " + repr(f_extns[-1]))