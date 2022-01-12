# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def give_str(sample_string, n):
    for i in range(n):
        print(sample_string)


give_str("Sentence", 5)

def larger_string(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result

print(larger_string("Sentence", 4))