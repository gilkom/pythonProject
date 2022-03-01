list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]

diff1 = list(set(list1) - set(list2))
print(diff1)

diff2 = list(set(list2) - set(list1))
print(diff2)

diff_list = list(diff1 + diff2)
print(diff_list)

list_as_set = set(list1)
print(list_as_set)
#
# result = list(set(list1).intersection(list2))
# print(result)