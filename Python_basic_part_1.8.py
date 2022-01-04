# 8. Write a Python program to display the first and last colors from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]

print(color_list[0] + " " + color_list[-1])

new_list = [color_list[0], color_list[-1]]
print(new_list)

print("%s %s" % (color_list[0],color_list[-1]))
