# 32. Write a Python program to get the least common multiple (LCM) of two positive integers.

def lcm(x, y):
    if x < y:
        lcm = y
    else:
        lcm = x
    while ((lcm % x) != 0 or ( lcm % y ) != 0):
        lcm +=1
    return lcm

# def lcm(x, y):
#   if x > y:
#       z = x
#   else:
#       z = y
#   while(True):
#       if((z % x == 0) and (z % y == 0)):
#           lcm = z
#           break
#       z += 1
#   return lcm




print(lcm(2, 3))
print(lcm(5, 10))
print(lcm(6, 8))
print(lcm(4, 6))
print(lcm(15, 17))