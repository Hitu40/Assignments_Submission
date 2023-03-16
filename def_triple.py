def triple(num):
    return num *3

nums = [1,2,3,4,5,6,7]
tripled_nums = list(map(triple, nums))


print(tripled_nums)

'''
Output: 
[3, 6, 9, 12, 15, 18, 21]
'''
