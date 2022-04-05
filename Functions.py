# 13 Write a Python function that prints out the first n rows of Pascal's triangle. Go to the editor
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
#
# Sample Pascal's triangle :
#
# Pascal's triangle
# Each number is the two numbers above it added together Go to the editor

# """"My solution"""
# def pascals_triangle(n):
#     tab = [1]
#     prev = []
#     print(tab)
#     for item in range(2, n+1):
#         row = []
#         if item == 2:
#             row = [1, 1]
#             prev = row
#         else:
#             length = len(prev) - 1
#             row.append(1)
#             for i in range(length):
#                 suma = prev[i] + prev[i+1]
#                 row.append(suma)
#             row.append(1)
#             prev = row
#
#         tab.append(row)
#         print(row)
#
#     return tab
#
#
# pascals_triangle(6)

"""Solution"""
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)
