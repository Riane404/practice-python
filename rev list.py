i=int(input("Enter the number of entries for list: "))
l=list()
c=0
for j in range(0,i):
    k=input("Enter the value for the list: ")
    l.append(k)
    
print()
print("The list in reverse is: ")
for r in range(0,i):
    c-=1
    print(l[c],end=" ")
    
    

