# 58. Write a Python program to sum of the first n positive integers.

# def sum_positive(n, *args):
#     count = n
#     sum = 0
#     print(count)
#     for arg in args:
#         if count > 0:
#             if arg > 0:
#                 sum = sum + arg
#                 count -= 1
#                 print("sum: ", sum)
#                 print("count: ", count)
#         else:
#             break
#
#     return sum
#
#
# print(sum_positive(3,-1,2,3,4,5,-6))

n = int(input("Input a number: "))
sum_num = (n * (n +1)) /2
print("Sum of the first", n, " positive integeres: ", sum_num)