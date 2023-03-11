#def function to sum all no in list
def sum_of_list(l):
    total=0
    for value in l:
        total=total + value
    return total

test_list = [8,2,3,0,7]
print("the sum of test_list is" , sum_of_list(test_list))