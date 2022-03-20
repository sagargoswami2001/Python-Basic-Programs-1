'''Write a Python Program to get the Command-line Arguments (name of the Script, the number 
of arguments, arguments) Passed to a Script.'''

import sys
print("This is the Name/Path of the Script: "),sys.argv[0]
print("Number of Arguments: ",len(sys.argv))
print("Argument List: ",str(sys.argv))