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
