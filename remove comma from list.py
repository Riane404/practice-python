i=input("Enter the values: ")
l=i.split(":")
l.remove(",")
t=tuple(l)
print()
print("List:",end="")
for k in l:
    print(k,end=" ")
print()
print("Tuple:",end="")
for s in t:
    print(s,end=" ")

