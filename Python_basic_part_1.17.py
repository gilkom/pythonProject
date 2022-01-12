# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

# numb = int(input("Write a number between 100 and 2000:"))
# if numb < 1000:
#    print("within 100 - 1000")
# else:
#     print("within 1001 - 2000")


def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))