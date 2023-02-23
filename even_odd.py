series = [1,2,3,4,5,6,7,8,9]

even_cnt = 0
odd_cnt = 0

for i in series:
    if(i % 2 == 0):
        even_cnt += 1
    else:
        odd_cnt += 1

print("Number of Even Numbers: ",even_cnt)
print("Number of Odd Numbers: ",odd_cnt)



