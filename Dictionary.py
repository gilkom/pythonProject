# !!! 1. Write a Python script to sort (ascending and descending) a dictionary
# by value.

# 1st solution with lambdas:

# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# d_sorted = sorted(d.items(), key= lambda kv: kv[1])
# print(dict(d_sorted))
# d_sorted = sorted(d.items(), key= lambda kv: kv[1], reverse=True)
# print(dict(d_sorted))

# 2nd solution with operator.itemgetter():

# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_d = dict(sorted(d.items(), key= operator.itemgetter(1)))
# print(sorted_d)
# sorted_d = dict(sorted(d.items(), key= operator.itemgetter(1), reverse=True))
# print(sorted_d)


# ------------------------------------------------------------------------
# !! 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# 1st my solution
# dic = {0: 10, 1: 20}
# dic[2]= 30
# print(dic)

# 2nd solution

# d = {0: 10, 1: 20}
# print(d)
# d.update({2: 30})
# print(d)

# ------------------------------------------------------------------------
# !!! 3. Write a Python script to concatenate following dictionaries to create
# a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
#
# for d in (dic1, dic2, dic3):
#     dic4.update(d)
# print(dic4)

# ------------------------------------------------------------------------
# 4. Write a Python script to check whether a given key already exists in
# a dictionary.

# 1st my solution
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print(1 in d)
# print(7 in d)

# 2nd solution
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#     if x in d:
#         print(True)
#     else:
#         print(False)
# is_key_present(5)
# is_key_present(9)

# ------------------------------------------------------------------------
# 5. Write a Python program to iterate over dictionaries using for loops.

# d = {'x': 10, 'y': 20, 'z': 30}
#
# for key, value in d.items():
#     print(f"{key} : {value}")

# ------------------------------------------------------------------------
# !!! 6. Write a Python script to generate and print a dictionary that contains
# a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 1st
# n = 5
# dictionary = {}
# for x in range(1, n + 1):
#     dictionary[x] = x*x
# print(dictionary)

# 2nd

# dictionary = {}
# for x in range(1, 6):
#     dictionary.update({x : x*x})
# print(dictionary)

# ------------------------------------------------------------------------
# 7. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
# 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# dictionary = {}
#
# for x in range(1, 16):
#     dictionary[x] = x*x
# print(dictionary)

# ------------------------------------------------------------------------
# ! 8. Write a Python script to merge two Python dictionaries.

# dict1 = {1: 'a', 2: 'b', 3: 'c'}
# dict2 = {3: 'd', 4: 'e'}
#
# d = dict1.copy()
# d.update(dict2)
# print(d)

# ------------------------------------------------------------------------
# 9. Write a Python program to iterate over dictionaries using for loops.

# dict1 = {1: 'a', 2: 'b', 3: 'c'}
# for d in dict1.items():
#     print(d)
# for k, v in dict1.items():
#     print(f"({k}, '{v}')")

# ------------------------------------------------------------------------
