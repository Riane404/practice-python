i=float(input("enter the 1st val: "))
j=float(input("enter the 2nd val: "))
k=float(input("enter the 3rd val: "))
l=float(input("enter the 4th val: "))

if (i>j)&(i>k)&(i>l):
    print(i," is the biggest number")

elif (j>i)&(j>k)&(j>l):
    print(j," is the biggest number")
    
elif (k>j)&(k>i)&(k>l):
    print(k," is the biggest number")
    
else:
    print(l,"is the biggest number")
