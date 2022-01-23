# # 52. Write a Python program to print to stderr.
# from __future__ import print_function
# import sys
# import os
#
#
# sys.stderr.write("spam\n")
#
# os.write(2, b"spam\n")
#
# print("spam", file=sys.stderr)

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")