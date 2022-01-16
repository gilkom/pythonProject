# 35. Write a Python program that will return true if the two given integer values are equal
# or their sum or difference is 5.

def fun_five(x, y):
    if(x == 5 or y == 5 or x + y == 5 or x - y == 5 or y - x == 5):
        return True
    return False


print(fun_five(3,2))
print(fun_five(3,5))
print(fun_five(6,1))
print(fun_five(1,2))
print(fun_five(7, 2))
print(fun_five(3, 2))
print(fun_five(2, 2))
print(fun_five(7, 3))
print(fun_five(27, 53))

