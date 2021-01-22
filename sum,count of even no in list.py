i=int(input("Enter the length of the list: "))
l=list()
c=0
s=0
for j in range(0,i):
    k=float(input("Enter the values to be entered: "))
    l.append(k)
    
print()

print("The even numbers are: ",end="")
for q in l:
    if q%2==0:
        s+=q
        c+=1
        print(q,end=" ")
print()
print("The count of the even numbers is %c"%c,c)
print("The sum of the even numbers is %s"%s)


    
