# 39. Write a Python program to compute the future value of a specified principal
# amount, rate of interest, and a number of years. Go to the editor
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def future_value(amt, rate, years):
    result = 10000
    for i in range(years):
        result = result + (( result  * rate)/100)
        print(result)


    return round(result,2)


print(future_value(10000, 3.5, 7))


# amt = 10000
# int = 3.5
# years = 7
# future_value = amt*((1+(0.01*int)) ** years)
# print(round(future_value,2))