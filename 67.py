# Write a Python Program to Get the Name of the Host on Which the Routine is Running.

import socket
host_name = socket.gethostname()
print()
print("Host Name:", host_name)
print()