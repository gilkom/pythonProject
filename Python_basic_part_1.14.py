# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
import datetime

date1 = datetime.date(2014, 7, 2)
date2 = datetime.date(2014, 7, 11)
result = date2 - date1
print(result.days)
