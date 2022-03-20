# Write a Python Program to Determine Profiling of Python Programs.

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')