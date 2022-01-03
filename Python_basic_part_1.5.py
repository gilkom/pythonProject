# . Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first = input("Write first name: ")[::-1]
last = input("Type last name: ")[::-1]
print(first + " " + last)

