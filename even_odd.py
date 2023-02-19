no = int(input("Enter a Number:"))

i = 1
even_cnt = 0
odd_cnt = 0
while i <= no:
    if(i % 2 == 0):
        even_cnt += 1
    else:
        odd_cnt += 1
    i += 1

print("Number of Even Numbers: ",even_cnt)
print("Number of Odd Numbers: ",odd_cnt)


'''
Output:

Enter a Number:35
Number of Even Numbers:  17
Number of Odd Numbers:  18
'''