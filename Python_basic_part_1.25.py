# 25. Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# def check_if_contains(n, m_list):
#     if n in m_list:
#         return True
#     else:
#         return False
#
# print(check_if_contains(3, [1, 3, 5]))
# print(check_if_contains(3, [1, 6, 5]))

def is_group_member(group_data, n):
    for val in group_data:
        if n == val:
            return True
    return False


print(is_group_member([1,5,8,3], 3))
print(is_group_member([5, 8, 3], -1))