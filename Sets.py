# 1. Write a Python program to create a set.

# s = set()
# print(s)
# print(type(s))
# n = set([1, 2, 3])
# print(n)
# print(type(n))
# a = {1, 2, 3, 4, 'foo', 'bar'}
# print(a)
# print(type(a))

# ------------------------------------------------------------------------
# 2. Write a Python program to iteration over sets.

# a = {1, 2, 3, 4, 'foo', 'bar'}
# for i in a:
#     print(i, end=' ')
#
# char_set = set({'w3resource', 'foo'})
# print(char_set)
#
# char_set2 = set('w3resource')
# for val in char_set2:
#     print(val, end=' ')
# print()

# ------------------------------------------------------------------------
# 3. Write a Python program to add member(s) in a set.

# s = set()
# s.add(1)
# print(s)
# s.update([1,2,3,4])
# print(s)

# ------------------------------------------------------------------------

# 4. Write a Python program to remove item(s) from a given set.

# a = {1, 2, 3, 5, 'ala'}
# print(a)
# a.remove(3)
# print(a)
# a.pop()
# print(a)

# ------------------------------------------------------------------------

# 5. Write a Python program to remove an item from a set if it is present
# in the set.

# a = set([1, 2, 3, 4, 5])
# print(a)
# a.discard(1)
# print(a)
# a.discard(7)
# print(a)

# ------------------------------------------------------------------------

# 6. Write a Python program to create an intersection of sets.
#
# a = {1, 2, 3}
# b = {2, 3, 4}
# c = a.intersection(b)
# print(c)
# d = a & b
# print(d)

# ------------------------------------------------------------------------

# 7. Write a Python program to create a union of sets.

# a = {1, 2, 3}
# b = {2, 3, 4}
#
# c = a.union(b)
# print(c)
# d = a | b
# print(d)

# ------------------------------------------------------------------------

# 8. Write a Python program to create set difference.
#
# a = {1, 2, 3}
# b = {2, 3, 4}
# c = a.difference(b)
# print(c)
# d = a - b
# print(d)

# ------------------------------------------------------------------------

# 9. Write a Python program to create a symmetric difference.
#
# a = {1, 2, 3}
# b = {2, 3, 4}
#
# c = a.symmetric_difference(b)
# print(c)