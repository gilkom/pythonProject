# # 37. Write a Python program to display your details like name, age, address in three different lines.
#
# def display_details(name, age, address):
#     print(name)
#     print(age)
#     print(address)
#
#
# display_details("Marcin", 33, "Pileckiego")
#
#

def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


personal_details()