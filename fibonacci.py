no = int(input("Enter a number: ")) # user input
x,y = 0,1

while y < no:
    print(y,end=" ")
    x,y = y,x+y
