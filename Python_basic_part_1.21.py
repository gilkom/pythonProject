# 21. Write a Python program to find whether a given
# number (accept from the user) is even or odd, print out an appropriate message to the user.

def even_or_odd():
    given_number = int(input("Write a number: "))
    if (given_number % 2) == 0:
        print("Given number is even")
    else:
        print("Giver number is odd")


even_or_odd()