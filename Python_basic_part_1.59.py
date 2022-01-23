# 59. Write a Python program to convert height (in feet and inches) to centimeters.

# number = float(input("Write number in feet and inches: "))
#
# result = 0
#
# rest = number
# rest = rest - int(number)
# rest = (round(rest *100) * 2.54)
#
# result = (int(number) * 30.48) + rest
#
# print(result)

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)