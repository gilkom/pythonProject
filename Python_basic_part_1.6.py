# 6. Write a Python program which accepts a sequence of comma-separated numbers from
# user and generate a list and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

numbers = input("Type few numbers separated with comma: ")
# numbers = numbers.replace(",", "")
n_list = numbers.split(",")
n_tuple = tuple(numbers.split(","))

print(numbers)
print(n_list)
print(n_tuple)