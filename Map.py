# 1. Write a Python program to triple all numbers of a given list of
# integers. Use Python map.

# li = [2, 4, 6, 9, 13]
#
# result = list(map(lambda x : x * 3, li))
# print(result)

# --------------------------------------------------------------------------

# 2. Write a Python program to add three given lists using Python map
# and lambda.

# a = [1, 2, 4]
# b = [4, 5, 6]
# c = [7, 8, 9]
#
# d = a + b + c
# print(d)
#
# e = list(map(lambda x, y, z: x + y + z, a, b, c))
# print(e)

# --------------------------------------------------------------------------

# !! 3. Write a Python program to listify the list of given strings individually
# using Python map.

# color = ['Red', 'Blue', 'Black', 'White', 'Pink']
#
# result = list(map(list, color))
# print(result)

# --------------------------------------------------------------------------

# 4. Write a Python program to create a list containing the power of
# said number in bases raised to the corresponding number in the index
# using Python map.

# bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# result = list(map(pow, bases_num, range(1, 11)))
# print(result)

# --------------------------------------------------------------------------

# 5. Write a Python program to square the elements of a list using map()
# function.

# nums = [4, 5, 2, 9]
#
# result = list(map(lambda x : x ** 2, nums))
# print(result)

# def square(x):
#     return x ** 2
#
# nums = [4, 5, 2, 9]
# result = list(map(square, nums))
# print(result)

# --------------------------------------------------------------------------

# 6. Write a Python program to convert all the characters in uppercase and
# lowercase and eliminate duplicate letters from a given sequence.
# Use map() function.