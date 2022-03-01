import itertools, time

start = time.time()
list(itertools.permutations([1,2,3]))
end = time.time()
print(f"3 elements: {end - start}")

start = time.time()
list(itertools.permutations([1,2,3,4,5]))
end = time.time()
print(f"5 elements: {end - start}")

start = time.time()
list(itertools.permutations([1,2,3,4,5,6,7]))
end = time.time()
print(f"7 elements: {end - start}")

start = time.time()
list(itertools.permutations([1,2,3,4,5,6,7,8,9,10]))
end = time.time()
print(f"10 elements: {end - start}")

start = time.time()
list(itertools.permutations([1,2,3,4,5,6,7,8,9,10,11]))
end = time.time()
print(f"11 elements: {end - start}")