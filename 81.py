# Write a Python Program to get an Absolute File Path.

def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')
print("Absolute File Path: ",absolute_file_path("test.txt"))