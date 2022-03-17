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
