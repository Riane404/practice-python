i=int(input("Enter the number of entries for int list: "))
l=list()
s=0
for j in range(0,i):
    k=float(input("Enter the value for the int list float is ok: "))
    l.append(k)
    s+=k
print()
print("The sum is %s"%s)
