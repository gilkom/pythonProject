# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math

r = float(input("Wpisz promień: "))
print(r)
result = math.pi * (r**2)
print("result =" + str(result))

