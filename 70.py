# Write a Python Program to Print to stderr.

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.__stderr__, **kwargs)

eprint("abc", "efg", "xyz", sep="--")