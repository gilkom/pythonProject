# 1. Write a Python program to create a tuple.

# x = ()
# print(x)
# # Create an empty tuple with tuple() function built-in Python
# tuplex = tuple()
# print(tuplex)

# -----------------------------------------------------------------------
# 2. Write a Python program to create a tuple with different data types.

# tup = (1, 1.1, 'bla', False)
# print(tup)
# print(type(tup))

# -----------------------------------------------------------------------
# 3. Write a Python program to create a tuple with numbers and print one item.

# tup = tuple(x for x in range(10))
# print(type(tup))
# print(tuple(tup))
# print(tup[0])
#
# tuplex = 5, 10, 15, 20, 25
# print(tuplex)
# print(type(tuplex))
# tuplex = 5,
# print(tuplex)
# print(type(tuplex))

# -----------------------------------------------------------------------

# 4. Write a Python program to unpack a tuple in several variables.

# tup = 1, 2, 3,
#
# one, two, three = tup
# print(tup)
# print(one)
# print(two)
# print(three)
# print(type(tup))
# print(type(one))
#
# tuplex = 4, 8, 3
# print(tuplex)
# n1, n2, n3 = tuplex
# #unpack a tuple in variables
# print(n1 + n2 + n3)
# #the number of variables must be equal to the number of items of the tuple
# n1, n2, n3, n4= tuplex

# -----------------------------------------------------------------------

# 5. Write a Python program to add an item in a tuple.

# tup = 1, 2, 3,
# print(tup)
# tup = tup + (4,)
# print(tup)
# print(type(tup))
#
# tup = tup[:2] + (44, 45, 46,) + tup[2:]
# print(tup)
#
# tup = list(tup)
# tup.append(300)
# tup = tuple(tup)
# print(tup)