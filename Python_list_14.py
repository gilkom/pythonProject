# numbers = [1, 2, 15, 5, 6, 219, 81, 5, 8, 22, 33]
# print(numbers)
# numbers = [x for x in numbers if not x % 2 != 0]
# print(numbers)

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(colors)

colors = [color for (i, color) in enumerate(colors) if i not in (0, 4, 5)]
print(colors)