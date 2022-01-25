# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

distance = int(input("Write distanece in feet: "))

inches = distance * 12
yards = round(distance * 0.33, 2)
miles = round(distance * 0.000189393939, 2)

print("inches: ", inches)
print("yards: ", yards)
print("miles: ", miles)