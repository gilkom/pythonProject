# 22. Write a Python program to count the number 4 in a given list.
my_list = [1, 2, 3, 4 , 3, 4 , 3, 4, 9, 4,7,4,8,2,1,3,4]

#  def count(list):
#     result = 0
#     for x in range(len(list)):
#         if list[x] == 4:
#             result += 1
#     return result
#
# print(count(my_list))

def count(list):
    result = 0
    for l in list:
        if l == 4:
            result += 1
    return result

print(count(my_list))