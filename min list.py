i=int(input("Enter the number of entries for int list: "))
l=list()

for j in range(0,i):
    k=float(input("Enter the value for the int list float is ok: "))
    l.append(k)

l.sort()
print()
print("The min val is %s"%l[0])
