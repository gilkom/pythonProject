# 14. Write a Python program to print the numbers of a specified list
# after removing even numbers from it.

# numbers = [1, 2, 15, 5, 6, 219, 81, 5, 8, 22, 33]
# print(numbers)
# numbers = [x for x in numbers if not x % 2 != 0]
# print(numbers)

# ------------------------------------------------------------

# 18. Write a Python program to generate all permutations of a list in Python.

# import itertools, time
#
# start = time.time()
# list(itertools.permutations([1,2,3]))
# end = time.time()
# print(f"3 elements: {end - start}")
#
# start = time.time()
# list(itertools.permutations([1,2,3,4,5]))
# end = time.time()
# print(f"5 elements: {end - start}")
#
# start = time.time()
# list(itertools.permutations([1,2,3,4,5,6,7]))
# end = time.time()
# print(f"7 elements: {end - start}")
#
# start = time.time()
# list(itertools.permutations([1,2,3,4,5,6,7,8,9,10]))
# end = time.time()
# print(f"10 elements: {end - start}")
#
# start = time.time()
# list(itertools.permutations([1,2,3,4,5,6,7,8,9,10,11]))
# end = time.time()
# print(f"11 elements: {end - start}")

# ------------------------------------------------------------
# 19. Write a Python program to get the difference between the two lists.
#
# list1 = [1, 3, 5, 7, 9]
# list2=[1, 2, 4, 6, 7, 8]
#
# diff1 = list(set(list1) - set(list2))
# print(diff1)
#
# diff2 = list(set(list2) - set(list1))
# print(diff2)
#
# diff_list = list(diff1 + diff2)
# print(diff_list)
#
# list_as_set = set(list1)
# print(list_as_set)
#
# result = list(set(list1).intersection(list2))
# print(result)