# 1. Write a Python program find a list of integers with exactly two
# occurrences of nineteen and at least three occurrences of five. Go to the editor
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True
#
# def occurancies(list):
#     five = 0
#     nineteen = 0
#     for i in list:
#         if i == 5:
#             five += 1
#         elif i == 19:
#             nineteen += 1
#     if(five >= 3 and nineteen == 2):
#         return True
#     return False

list1 = [19, 19, 15, 5, 3, 5, 5, 2]
list2 = [19, 15, 15, 5, 3, 3, 5, 2]
list3 = [19, 19, 5, 5, 5, 5, 5]

def occurancies(list):
    return list.count(5) >= 3 and list.count(19) == 2

print(occurancies(list1))
print(occurancies(list2))
print(occurancies(list3))