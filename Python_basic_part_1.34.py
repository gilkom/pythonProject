# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def two_sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    return sum


print(two_sum(5,14))
print(two_sum(1,10))
print(two_sum(10, 6))
print(two_sum(10, 2))
print(two_sum(10, 12))