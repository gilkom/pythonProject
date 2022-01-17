# 38. Write a Python program to solve (x + y) * (x + y). Go to the editor
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

def solve(x, y):
    #return (x + y) * (x + y)
    #return (x + y) ** 2
    result = (x + y) ** 2
    return ("({} + {}) ^ 2) = {}".format(x, y, result))


print(solve(4, 3))