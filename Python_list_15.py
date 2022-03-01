squares = list(range(1, 31))
print(squares)
l = list()

for s in squares:
    l.append(s**2)

print(l)

l = [x for (i, x) in enumerate(l) if i < 5 or i > 25]
print(l)