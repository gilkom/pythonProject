# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

# def n_copies(strin, n):
#     result = ""
#     if len(strin) < 2:
#         for s in range(n):
#             result = result + strin
#     else:
#         for s in range(n):
#             result = result + strin[0] + strin[1]
#     return result
#
#
# print(n_copies("something", 5))
# print(n_copies("x", 5))


def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result


print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));
