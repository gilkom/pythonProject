# 2. Write a Python program that accept a list of integers and check the length and
# the fifth element. Return true if the length of the list is 8 and fifth element
# occurs thrice in the said list. Go to the editor
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:
# False
# Input:
# [11, 12, 14, 13, 14, 13, 15, 14]
# Output:
# True
# Input:
# [19, 15, 11, 7, 5, 6, 2]
# Output:
# False

def test(list):
    return len(list) == 8 and list.count((list[4])) == 3


list1 = [19, 19, 15, 5, 5, 5, 1, 2]
list2 = [19, 15, 5, 7, 5, 5, 2]
list3 = [11, 12, 14, 13, 14, 13, 15, 14]
list4 = [19, 15, 11, 7, 5, 6, 2]

print(test(list1))
print(test(list2))
print(test(list3))
print(test(list4))