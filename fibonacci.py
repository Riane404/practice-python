b=int(input("Enter the number of values of the series needed: "))
i=0
j=1
k=0
s=2
print (i,j,end=" ")
for s in range(2,b):
    k=j+i
    print(k,end=" ")
    i=j
    j=k
    
