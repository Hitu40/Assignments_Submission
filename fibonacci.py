no = int(input("Enter a number: "))
x,y = 0,1

while y < no:
    print(y,end=" ")
    x,y = y,x+y

'''
Output

Enter a number: 50
1 1 2 3 5 8 13 21 34 

'''
