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

# ----------------------------------------------------------------------------

# # 22. Write a Python program to count the number 4 in a given list.
# my_list = [1, 2, 3, 4 , 3, 4 , 3, 4, 9, 4,7,4,8,2,1,3,4]
#
# #  def count(list):
# #     result = 0
# #     for x in range(len(list)):
# #         if list[x] == 4:
# #             result += 1
# #     return result
# #
# # print(count(my_list))
#
# def count(list):
#     result = 0
#     for l in list:
#         if l == 4:
#             result += 1
#     return result
#
# print(count(my_list))
#
# # ----------------------------------------------------------------------------
#
# # 23. Write a Python program to get the n (non-negative integer) copies of
# the first 2 characters of a given string.
# # Return the n copies of the whole string if the length is less than 2.
#
# # def n_copies(strin, n):
# #     result = ""
# #     if len(strin) < 2:
# #         for s in range(n):
# #             result = result + strin
# #     else:
# #         for s in range(n):
# #             result = result + strin[0] + strin[1]
# #     return result
# #
# #
# # print(n_copies("something", 5))
# # print(n_copies("x", 5))
#
#
# def substring_copy(str, n):
#     flen = 2
#     if flen > len(str):
#         flen = len(str)
#     substr = str[:flen]
#
#     result = ""
#     for i in range(n):
#         result = result + substr
#     return result
#
#
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3));
#
# # ------------------------------------------------------------------------
#
# # 24. Write a Python program to test whether a passed letter is a vowel
# or not.
#
# # def vowel(l):
# #     vowels = "aeiouy"
# #     if l in vowels:
# #         return "yes"
# #     else:
# #         return "no"
# #
# # print(vowel('a'))
# # print(vowel('z'))
#
#
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
#
#
# print(is_vowel('c'))
# print(is_vowel('e'))
#
# ------------------------------------------------------------------------
#
# # 25. Write a Python program to check whether a specified value is
# contained in a group of values.
# # Test Data :
# # 3 -> [1, 5, 8, 3] : True
# # -1 -> [1, 5, 8, 3] : False
#
# # def check_if_contains(n, m_list):
# #     if n in m_list:
# #         return True
# #     else:
# #         return False
# #
# # print(check_if_contains(3, [1, 3, 5]))
# # print(check_if_contains(3, [1, 6, 5]))
#
# def is_group_member(group_data, n):
#     for val in group_data:
#         if n == val:
#             return True
#     return False
#
#
# print(is_group_member([1,5,8,3], 3))
# print(is_group_member([5, 8, 3], -1))
#
# # ------------------------------------------------------------------------
#
# # 26. Write a Python program to create a histogram from a given list of
# integers.
#
# # def histogram_from_list(my_list):
# #     for i in my_list:
# #         result = ""
# #         for val in range(i):
# #             result = result + "*"
# #         print(result)
# #
# #
# # histogram_from_list([4, 7, 1, 4])
#
#
# def histogram( items ):
#     for n in items:
#         output = ''
#         times = n
#         while( times > 0 ):
#             output += '*'
#             times = times - 1
#         print(output)
#
#
# histogram([2, 3, 6, 5])
#
# ------------------------------------------------------------------------
#
# # Write a Python program to concatenate all elements in a list into a string
# and return it.
#
# # my_list = ["pierwszy", "drugi", "trzeci", "czwarty"]
# #
# # def concatenate(my_list):
# #     result = ""
# #     for i in my_list:
# #         result = result + i
# #     return result
# #
# # print(concatenate(my_list))
#
# def concatenate_list_data(list):
#     result = ""
#     for element in list:
#         result += str(element)
#     return result
#
#
# print(concatenate_list_data([1, 5, 12, 2]))
#
# # ------------------------------------------------------------------------
#
# # 28. Write a Python program to print all even numbers from a given numbers
# list in the
# # same order and stop the printing if any numbers that come after 237 in the
# sequence. Go to the editor
# # Sample numbers list :
# #
# # numbers = [
# 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
# 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
# 687, 217,
# 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
# 742, 717,
# 958,743, 527
# #     ]
# numbers = [
#      386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
#      953, 345,
#      399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
#      687, 217,
#      815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831,
#      445, 742, 717,
#      958,743, 527
#      ]
#
# def print_even_numbers(list):
#     for i in list:
#         if i == 237:
#             print(i)
#             break
#         elif (i % 2) == 0:
#             print(i, end=', ')
#
# print_even_numbers(numbers)
#
# # ------------------------------------------------------------------------
#
# # 29. Write a Python program to print out a set containing
# # all the colors from color_list_1 which are not present in color_list_2.
# # Test Data :
# # color_list_1 = set(["White", "Black", "Red"])
# # color_list_2 = set(["Red", "Green"])
# # Expected Output :
# # {'Black', 'White'}
# # color_list_1 = set(["White", "Black", "Red"])
# # color_list_2 = set(["Red", "Green"])
# #
# # def print_colors(list1, list2):
# #     for i in list1:
# #         if i not in list2:
# #             print(i, end=" ")
# #     print("")
# #
# #
# # print_colors(color_list_1, color_list_2)
#
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
#
# print(color_list_1.difference(color_list_2))
#
# # ------------------------------------------------------------------------
#
# # 30. Write a Python program that will accept the base and height of a
# triangle and compute the area.
#
# def calculate_triangle_area(base, heigth):
#     return (base * heigth)/2
#
#
# print(calculate_triangle_area(5, 20))
#
# ------------------------------------------------------------------------
#
# # 31. Write a Python program to compute the greatest common divisor (GCD)
# of two positive integers.
#
#
# # def gcd(num1, num2):
# #     while num2 != 0:
# #         res = num2
# #         num2 = num1 % num2
# #         num1 = res
# #     return num1
#
#
# def gcd(x ,y):
#     gcd = 1
#     if x % y == 0:
#         return y
#     for k in range(int(y / 2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
#     return gcd
#
#
# print("GCD of 12 & 17 =",gcd(12, 17))
# print("GCD of 4 & 6 =",gcd(4, 6))
# print("GCD of 336 & 360 =",gcd(336, 360))
#
# ------------------------------------------------------------------------

# 32. Write a Python program to get the least common multiple (LCM) of two
# positive integers.
#
# def lcm(x, y):
#     if x < y:
#         lcm = y
#     else:
#         lcm = x
#     while ((lcm % x) != 0 or ( lcm % y ) != 0):
#         lcm +=1
#     return lcm
#
# # def lcm(x, y):
# #   if x > y:
# #       z = x
# #   else:
# #       z = y
# #   while(True):
# #       if((z % x == 0) and (z % y == 0)):
# #           lcm = z
# #           break
# #       z += 1
# #   return lcm
#
#
#
#
# print(lcm(2, 3))
# print(lcm(5, 10))
# print(lcm(6, 8))
# print(lcm(4, 6))
# print(lcm(15, 17))
#
# # ----------------------------------------------------------------------------
#
# # 33. Write a Python program to sum of three given integers. However, if
# two values are equal sum will be zero.
#
# def three_sum(x, y, z):
#     if(x == y or x == z or y == z):
#         return 0
#     return x + y + z
#
#
# print(three_sum(1, 2, 3))
# print(three_sum(1, 3, 3))
# print(three_sum(2, 1, 2))
# print(three_sum(3, 2, 2))
# print(three_sum(2, 2, 2))
# print(three_sum(1, 2, 3))
#
# # ------------------------------------------------------------------------
#
# # 34. Write a Python program to sum of two given integers. However,
# if the sum is between 15 to 20 it will return 20.
#
# def two_sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     return sum
#
#
# print(two_sum(5,14))
# print(two_sum(1,10))
# print(two_sum(10, 6))
# print(two_sum(10, 2))
# print(two_sum(10, 12))
#
# # ------------------------------------------------------------------------
#
# # 35. Write a Python program that will return true if the two given
# integer values are equal
# # or their sum or difference is 5.
#
# def fun_five(x, y):
#     if(x == 5 or y == 5 or x + y == 5 or x - y == 5 or y - x == 5):
#         return True
#     return False
#
#
# print(fun_five(3,2))
# print(fun_five(3,5))
# print(fun_five(6,1))
# print(fun_five(1,2))
# print(fun_five(7, 2))
# print(fun_five(3, 2))
# print(fun_five(2, 2))
# print(fun_five(7, 3))
# print(fun_five(27, 53))
#
#
# # # ------------------------------------------------------------------------
#
# # 36. Write a Python program to add two objects if both objects are an
# integer type.
#
# def if_integer_add(x, y):
#     if(isinstance(x, int) and isinstance(y, int)):
#         return x + y
#     else:
#         return "not integer"
#
#
# print(if_integer_add(13, 2))
# print(if_integer_add(10, 20))
# print(if_integer_add(10, 20.23))
# print(if_integer_add('5', 6))
# print(if_integer_add('5', '6'))
#
# # # ------------------------------------------------------------------------
#
# # # 37. Write a Python program to display your details like name, age,
# address in three different lines.
# #
# # def display_details(name, age, address):
# #     print(name)
# #     print(age)
# #     print(address)
# #
# #
# # display_details("Marcin", 33, "Pileckiego")
# #
# #
#
# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
#
#
# personal_details()
#
# # # ------------------------------------------------------------------------
#
# # 38. Write a Python program to solve (x + y) * (x + y). Go to the editor
# # Test Data : x = 4, y = 3
# # Expected Output : (4 + 3) ^ 2) = 49
#
# def solve(x, y):
#     #return (x + y) * (x + y)
#     #return (x + y) ** 2
#     result = (x + y) ** 2
#     return ("({} + {}) ^ 2) = {}".format(x, y, result))
#
#
# print(solve(4, 3))
#
# # ------------------------------------------------------------------------
#
# # 39. Write a Python program to compute the future value of a specified
# principal
# # amount, rate of interest, and a number of years. Go to the editor
# # Test Data : amt = 10000, int = 3.5, years = 7
# # Expected Output : 12722.79
#
# def future_value(amt, rate, years):
#     result = 10000
#     for i in range(years):
#         result = result + (( result  * rate)/100)
#         print(result)
#
#
#     return round(result,2)
#
#
# print(future_value(10000, 3.5, 7))
#
#
# # amt = 10000
# # int = 3.5
# # years = 7
# # future_value = amt*((1+(0.01*int)) ** years)
# # print(round(future_value,2))
#
# # ------------------------------------------------------------------------
#
# # 40. Write a Python program to compute the distance between the
# points (x1, y1) and (x2, y2).
# import math
#
#
# def distance(x1, y1, x2, y2):
#     return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
#
#
# print(distance(4, 0, 6, 6))
#
#
#
# # 41. Write a Python program to check whether a file exists
#
# import os.path
# def is_file(name):
#     if(os.path.isfile(name)):
#         return 'True'
#     else:
#         return 'False'
#
#
# print(is_file('./bla.txt'))
# print(is_file('./main.py'))
# print(is_file('./blabla.txt'))
# print(is_file('./Python_basic_part_1.10.py'))
# print(is_file('./Python_basic_part_1.43'))
# # ------------------------------------------------------------------------
