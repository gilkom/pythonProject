# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.


# def gcd(num1, num2):
#     while num2 != 0:
#         res = num2
#         num2 = num1 % num2
#         num1 = res
#     return num1


def gcd(x ,y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd


print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

