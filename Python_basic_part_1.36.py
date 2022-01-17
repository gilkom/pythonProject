# 36. Write a Python program to add two objects if both objects are an integer type.

def if_integer_add(x, y):
    if(isinstance(x, int) and isinstance(y, int)):
        return x + y
    else:
        return "not integer"


print(if_integer_add(13, 2))
print(if_integer_add(10, 20))
print(if_integer_add(10, 20.23))
print(if_integer_add('5', 6))
print(if_integer_add('5', '6'))