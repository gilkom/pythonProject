# 57. Write a Python program to get execution time for a Python method.

import time

def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s = s + 1
    end_time = time.time()
    return s, end_time-start_time


n = 5
print("Time to sum of 1 to ", n, " and required time to calculate is :", sum_of_n_numbers(n))
print("Time to sum of 1 to ", 100, " and required time to calculate is :", sum_of_n_numbers(100))
print("Time to sum of 1 to ", 10000, " and required time to calculate is :", sum_of_n_numbers(10000))
print("Time to sum of 1 to ", 1000000, " and required time to calculate is :", sum_of_n_numbers(1000000))
print("Time to sum of 1 to ", 10000000, " and required time to calculate is :", sum_of_n_numbers(10000000))
print("Time to sum of 1 to ", 100000000, " and required time to calculate is :", sum_of_n_numbers(100000000))
print("Time to sum of 1 to ", 200000000, " and required time to calculate is :", sum_of_n_numbers(200000000))
print("Time to sum of 1 to ", 400000000, " and required time to calculate is :", sum_of_n_numbers(400000000))
