# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.

# seconds = int(input("Write seconds: "))
#
# minutes = seconds / 60
# hours = minutes / 60
# days = hours / 24
#
# print("minutes: ",  minutes)
# print("hours: ", hours)
# print("days: ", days)

time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))