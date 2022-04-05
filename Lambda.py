# 1. Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that
# multiplies argument x with argument y and print the result.
# Sample Output:
# 25
# 48
#
# r = lambda x : x + 15
# print(r(9))
# r = lambda x, y : x * y
# print(r(3, 3))

# ---------------------------------------------------------------------------

# 2. Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
# 75
# def fun(n):
#     return lambda x : x * n
#
# result = fun(15)
# print(f"Double the number of 15: {result(2)}")
# result = fun(15)
# print(f"Triple the number of 15: {result(3)}")
# result = fun(15)
# print(f"Quadruple the number of 15: {result(4)}")
# result = fun(15)
# print(f"Quintuple the number of 15: {result(5)}")

# ---------------------------------------------------------------------------

# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# tup = [('English', 88), ('Science', 90), ('Maths', 97),
# ('Social sciences', 82)]
#
# tupl = list(sorted(tup, key = lambda x : x[1]))
# print(tupl)
# print(tup)
#
# tup.sort(key = lambda x : x[1])
# print(tup)

# ---------------------------------------------------------------------------

# 4. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max',
# 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7,
# 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung',
# 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2',
# 'color': 'Gold'}]
#
# phones = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# phones_sorted = list(sorted(phones, key=lambda x: x['color']))
# print(phones_sorted)
#
# print(phones)
# phones.sort(key=lambda x: x['color'])
# print(phones)

# ---------------------------------------------------------------------------

# 5. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(numbers)
# even = list(filter(lambda x : x % 2 == 0, numbers))
# print(even)
#
# odd = list(filter(lambda x : x % 2 != 0, numbers))
# print(odd)

# ---------------------------------------------------------------------------

# 6. Write a Python program to square and cube every number in a given list
# of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# squares = list(map(lambda x : x * x, numb))
# print(squares)
#
# cubes = list(map(lambda x : x ** 3, numb))
# print(cubes)

# ---------------------------------------------------------------------------

# !!! 7. Write a Python program to find if a given string starts with a
# given character using Lambda.
# Sample Output:
# True
# False
#
#
# r = lambda x : x.startswith('Z')
# print(r('Zupa'))
#
# r = lambda x : x.startswith('z')
# print(r('Zupa'))

# ---------------------------------------------------------------------------

# 8. Write a Python program to extract year, month, date and time using Lambda.
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# from datetime import datetime
#
# data = datetime.now()
# print(data)
# r = lambda x : x.year
# print(r(data))
# r = lambda x : x.month
# print(r(data))
# r = lambda x : x.day
# print(r(data))
# r = lambda x : x.time()
# print(r(data))

# ---------------------------------------------------------------------------

# ! 9. Write a Python program to check whether a given string is number or not
# using Lambda.
# Sample Output:
# True
# True
# False
# True
# False
# True
# Print checking numbers:
# True
# True

# is_num = lambda x : x.replace('.','',1).isdigit()
#
# print(is_num('26587'))
# print(is_num('4.2365'))
# print(is_num('-12547'))
# print(is_num('00'))
# print(is_num('A001'))
# print(is_num('001'))
#
# is_num1 = lambda x : is_num(x[1:]) if x[0] == '-' else is_num(x)
#
# print(is_num1('-16.4'))
# print(is_num1('-24587.11'))
# print(is_num1('-12547'))

# ---------------------------------------------------------------------------

# !!!!10. Write a Python program to create Fibonacci series upto n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]

# fib = []
# for num in range(9):
#     if len(fib) > 1:
#         res = fib[-2] + fib[-1]
#         fib.append(res)
#     elif len(fib) == 0:
#         fib.append(0)
#     elif len(fib) == 1:
#         fib.append(1)
# print(fib)

# right solution:

# from functools import reduce
#
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
#                               range(n - 2), [0, 1])
#
# print("Fibonacci series upto 2:")
# print(fib_series(2))
# print("\nFibonacci series upto 5:")
# print(fib_series(5))
# print("\nFibonacci series upto 6:")
# print(fib_series(6))
# print("\nFibonacci series upto 9:")
# print(fib_series(9))

# ---------------------------------------------------------------------------

# !!! 11. Write a Python program to find intersection of two given arrays using
# Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

# a = [1, 2, 3, 5, 7, 8, 9, 10]
# b =  [1, 2, 4, 8, 9]
#
# lam = list(filter(lambda x: x in a, b ))
# print(lam)

# a = [1, 2, 3, 5, 7, 8, 9, 10]
# b =  [1, 2, 4, 8, 9]
#
# intersec = list(set(a) & set(b))
# print(intersec)

# ---------------------------------------------------------------------------
# 12. Write a Python program to rearrange positive and negative numbers in a
# given array using Lambda.
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]

# array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
# print("Original arrays:")
# print(array_nums)
# result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
# print("\nRearrange positive and negative numbers of the said array:")
# print(result)

# ---------------------------------------------------------------------------

# 13. Write a Python program to count the even, odd numbers in a given array
# of integers using Lambda. Go to the editor
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

# a =  [1, 2, 3, 5, 7, 8, 9, 10]
#
# even = len(list(filter(lambda x : x % 2 == 0, a)))
# print(even)
#
# odd = len(list(filter(lambda x : x % 2 != 0, a)))
# print(odd)

# --------------------------------------------------------------------------

