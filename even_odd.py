no = int(input("Enter a Number:"))

i = 1
even_cnt = 0
odd_cnt = 0
while i <= no:
    print(i)
    if(i % 2 == 0):
        even_cnt += 1
    else:
        odd_cnt += 1
    i += 1

print("Number of Even Numbers: ",even_cnt)
print("Number of Odd Numbers: ",odd_cnt)


'''
Enter a Number:9

1
2
3
4
5
6
7
8
9

Number of Even Numbers:  4
Number of Odd Numbers:  5
'''
