i=int(input("Enter the number of columns: "))
j=int(input("Enter the number of rows: "))
for col in range(0,i):
    s=col+1
    cs=s
    c=cs
    for row in range(0,j):
        print(cs,end=" ")
        cs+=c
         
    print()
