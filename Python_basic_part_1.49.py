# 49. Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import isfile, join
# print(os.listdir())

files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
print(files_list);
