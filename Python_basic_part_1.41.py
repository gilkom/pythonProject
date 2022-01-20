# 41. Write a Python program to check whether a file exists

import os.path
def is_file(name):
    if(os.path.isfile(name)):
        return 'True'
    else:
        return 'False'


print(is_file('./bla.txt'))
print(is_file('./main.py'))
print(is_file('./blabla.txt'))
print(is_file('./Python_basic_part_1.10.py'))
print(is_file('./Python_basic_part_1.43'))
