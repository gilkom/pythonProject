# 18. Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.

val1 = int(input("val1:"))
val2 = int(input("val2:"))
val3 = int(input("val3:"))

if val1 == val2 and val2 == val3:
    print(3*(val1 + val2 + val3))
else:
    print(val1 + val2 + val3)


# def sum_thrice(x, y, z):

#     sum = x + y + z

#     if x == y == z:
#      sum = sum * 3
#     return sum

# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))
