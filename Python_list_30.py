def count_elements(li, min, max):
    counter = 0
    for item in li:
        if item >= min and item <=max:
            counter +=1
    return counter


list1 = [10,20,30,40,40,40,70,80,99]
list2 = ['a','b','c','d','e','f']
print(count_elements(list1, 40, 100))
print(count_elements(list2, 'a', 'e'))
