# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def three_sum(x, y, z):
    if(x == y or x == z or y == z):
        return 0
    return x + y + z


print(three_sum(1, 2, 3))
print(three_sum(1, 3, 3))
print(three_sum(2, 1, 2))
print(three_sum(3, 2, 2))
print(three_sum(2, 2, 2))
print(three_sum(1, 2, 3))

