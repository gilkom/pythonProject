# Write a Python program to concatenate all elements in a list into a string and return it.

# my_list = ["pierwszy", "drugi", "trzeci", "czwarty"]
#
# def concatenate(my_list):
#     result = ""
#     for i in my_list:
#         result = result + i
#     return result
#
# print(concatenate(my_list))

def concatenate_list_data(list):
    result = ""
    for element in list:
        result += str(element)
    return result


print(concatenate_list_data([1, 5, 12, 2]))