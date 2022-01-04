# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

y = int(input("Type year: "))
m = int(input("Typ month: "))

print(calendar.month(y, m))
print(calendar.calendar(y))