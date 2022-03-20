# Write a Python Program to get the Path and Name of the file that is Currently Executing.

import os
print("Current File Name: ",os.path.realpath(__file__))