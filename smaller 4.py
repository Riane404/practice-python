i=float(input("Enter the 1st val: "))
j=float(input("Enter the 2nd val: "))
k=float(input("Enter the 3rd val: "))
l=float(input("Enter the 4th val: "))
print("")

if (i<j)&(i<k)&(i<l):
    print(i," is the smallest val")

elif (j<i)&(j<k)&(j<l):
    print(j," is the smallest val")

elif (k<i)&(k<j)&(k<l):
    print(k," is the smallest val")

else:
    print(l," is the smallest val")
