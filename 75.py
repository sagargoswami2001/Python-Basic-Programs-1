# Write a Python Program to get execution time (in seconds) for a Python Method.

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to Sum of 1 to ",n," and Required time to Calculate is :",sum_of_n_numbers(n))