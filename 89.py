# Write a Python Program to Get a Directory Listing, Sorted By Creation Date.

from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

# Relative or Absolute Path to the Directory
dir_path = sys.argv[1] if len(sys.argv)  == 2 else r'.'

# All Entries in the Directory w/ Stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# Regular Files, Insert Creation Date
data = ((stat[ST_CTIME], path)
            for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))
