# 1. Write a Python program to print the following string in a specific format
# (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are!
# Up above the world so high, Like a diamond in the sky. Twinkle,
# twinkle, little star, How I wonder what you are" Output :
#
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are
#
# print("Twinkle, twinkle, little star, \n\t"
#       "How I wonder what you are! \n\t\t"
#       "Up above the world so high, \n\t\t"
#       "Like a diamond in the sky. \n"
#       "Twinkle, twinkle, little star, \n\t"
#       "How I wonder what you are")

# ----------------------------------------------------------------------------
# 2. Write a Python program to get the Python version you are using.
#
# import sys
# print("Python version: ")
# print(sys.version)
# print("Python Version info.: ")
# print(sys.version_info)
# print("other: ")
# print(sys.prefix)
# print(sys.path)
# print(sys.api_version)
# print(sys.copyright)
# print(sys.getallocatedblocks())
# print(sys.platform)
# print(sys.getprofile())
# print(sys.byteorder)
# print(sys.implementation)
#
# --------------------------------------------------------------------
# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# import datetime
#
# today = datetime.datetime.now()
#
# print("Current date and time ")
# print(today)

# ----------------------------------------------------------------------------

# 4. Write a Python program which accepts the radius of a circle from the user
# and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
#
# import math
#
# r = float(input("Wpisz promień: "))
# print(r)
# result = math.pi * (r**2)
# print("result =" + str(result))

# ----------------------------------------------------------------------------

# 5 Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.

# first = input("Write first name: ")[::-1]
# last = input("Type last name: ")[::-1]
# print(first + " " + last)

# ----------------------------------------------------------------------------

# 6. Write a Python program which accepts a sequence of comma-separated
# numbers from
# user and generate a list and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
#
# numbers = input("Type few numbers separated with comma: ")
# # numbers = numbers.replace(",", "")
# n_list = numbers.split(",")
# n_tuple = tuple(numbers.split(","))
#
# print(numbers)
# print(n_list)
# print(n_tuple)

# ----------------------------------------------------------------------------

# 7. Write a Python program to accept a filename from the user and print the
# extension of that.
# Sample filename : abc.java
# Output : java
#
# my_string = input("Insert file with extension: ")
#
# # print(my_string.split(".", 1)[1])
# print(my_string.split(".")[-1])

# ----------------------------------------------------------------------------

# 8. Write a Python program to display the first and last colors from the
# following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]

# color_list = ["Red","Green","White" ,"Black"]
#
# print(color_list[0] + " " + color_list[-1])
#
# new_list = [color_list[0], color_list[-1]]
# print(new_list)
#
# print("%s %s" % (color_list[0],color_list[-1]))

# ----------------------------------------------------------------------------

# 9. Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

# exam_st_date = (11, 12, 2014)
# print("The examination will start from: ", end='')
# for i in exam_st_date:
#     print(i, end=' / ')
# print()
# print("The examination will start from: %i / %i / %i"% exam_st_date)


# ----------------------------------------------------------------------------

# 10. Write a Python program that accepts an integer (n) and computes the
# value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

# n = str(input("Type number: "))
# nn = n + n
# nnn = n + n + n
# print(int(n) + int(nn) + int(nnn))
#
# a = int(input("Input an integer : "))
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# ----------------------------------------------------------------------------

# 11. Write a Python program to print the documents (syntax, description etc.)
# of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
#
# print(abs.__doc__)
# print(all.__doc__)

# ----------------------------------------------------------------------------

# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

# import calendar
#
# y = int(input("Type year: "))
# m = int(input("Typ month: "))
#
# print(calendar.month(y, m))
# print(calendar.calendar(y))

# ----------------------------------------------------------------------------

# 13. Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
#
# print("""a string that you "don't" have to escape""")
# print("This")
# print("is a ...... multi-line")
# print("heredoc string ------> example")
#
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)

# ----------------------------------------------------------------------------


# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# import datetime
#
# date1 = datetime.date(2014, 7, 2)
# date2 = datetime.date(2014, 7, 11)
# result = date2 - date1
# print(result.days)

# ----------------------------------------------------------------------------


# 15. Write a Python program to get the volume of a sphere with radius 6.
# import math
#
# r = int(input("Type radius"))
# volume = (4 * math.pi * r**3)/3
# print(volume)

# ----------------------------------------------------------------------------

# 16. Write a Python program to get the difference between a given number
# and 17,
# if the number is greater than 17 return double the absolute difference.
#
# x = int(input("Type number: "))
# if x > 17:
#     print(abs(17 - x) * 2)
# else:
#     print(17 - x)

# ----------------------------------------------------------------------------

# 17. Write a Python program to test whether a number is within 100 of 1000
# or 2000.

# numb = int(input("Write a number between 100 and 2000:"))
# if numb < 1000:
#    print("within 100 - 1000")
# else:
#     print("within 1001 - 2000")

#
# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
#
#
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))

# ----------------------------------------------------------------------------

# 18. Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum.
#
# val1 = int(input("val1:"))
# val2 = int(input("val2:"))
# val3 = int(input("val3:"))
#
# if val1 == val2 and val2 == val3:
#     print(3*(val1 + val2 + val3))
# else:
#     print(val1 + val2 + val3)


# def sum_thrice(x, y, z):

#     sum = x + y + z

#     if x == y == z:
#      sum = sum * 3
#     return sum

# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))

# ----------------------------------------------------------------------------

# 19. Write a Python program to get a new string from a given string where
# "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.
#
# text = input("Type new string: ")
#
# if text[0] == "I" and text[1] == "s":
#     print(text)
# else:
#     text="Is" + text
#     print(text)


# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str
#
# print(new_string("Array"))
# print(new_string("IsEmpty"))

# ----------------------------------------------------------------------------

# 20. Write a Python program to get a string which is n (non-negative integer)
# copies of a given string.
#
# def give_str(sample_string, n):
#     for i in range(n):
#         print(sample_string)
#
#
# give_str("Sentence", 5)
#
# def larger_string(str, n):
#     result = ""
#     for i in range(n):
#         result = result + str
#     return result
#
# print(larger_string("Sentence", 4))

# ----------------------------------------------------------------------------

# 21. Write a Python program to find whether a given
# number (accept from the user) is even or odd, print out an appropriate
# message to the user.
#
# def even_or_odd():
#     given_number = int(input("Write a number: "))
#     if (given_number % 2) == 0:
#         print("Given number is even")
#     else:
#         print("Giver number is odd")
#
#
# even_or_odd()
