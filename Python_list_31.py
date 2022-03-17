my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print(my_list)

my_dictionary = {}

for item in my_list:
    if item not in my_dictionary.keys():
        my_dictionary[item] = 1
    else:
        my_dictionary[item] = my_dictionary[item] + 1


print(my_dictionary)

