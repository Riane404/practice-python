i=int(input("Enter the number of rows: "))
j=int(input("Enter the number of columns: "))
for row in range(1,i+1):
    s=row
    c=s
    for col in range(0,j):
        print(s,end="  ")
        s+=c  
    print()
    print()
