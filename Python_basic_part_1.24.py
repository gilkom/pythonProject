# 24. Write a Python program to test whether a passed letter is a vowel or not.

# def vowel(l):
#     vowels = "aeiouy"
#     if l in vowels:
#         return "yes"
#     else:
#         return "no"
#
# print(vowel('a'))
# print(vowel('z'))


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


print(is_vowel('c'))
print(is_vowel('e'))