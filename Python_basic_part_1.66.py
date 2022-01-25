# 66. Write a Python program to calculate body mass index.

weight = int(input("Write weight in kg: "))
height = int(input("Write heigth in metres:"))

bmi = weight / ((height/100)**2)
print(bmi)