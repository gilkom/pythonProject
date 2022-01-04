# 7. Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

my_string = input("Insert file with extension: ")

# print(my_string.split(".", 1)[1])
print(my_string.split(".")[-1])



