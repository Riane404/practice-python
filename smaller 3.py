i=float(input("Enter the 1st val: "))
j=float(input("Enter the 2nd val: "))
k=float(input("Enter the 3rd val: "))
print("")

if (i<j)&(i<k):
    print(i," is the smallest val")

elif (j<i)&(j<k):
    print(j," is the smallest val")

else:
    print(k," is the smallest val")
