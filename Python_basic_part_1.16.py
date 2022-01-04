# 16. Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

x = int(input("Type number: "))
if x > 17:
    print(abs(17 - x) * 2)
else:
    print(17 - x)
