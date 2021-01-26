i=int(input("Enter the length of the tuple: "))
l=list()
for j in range(0,i):
    k=int(input("Enter the values: "))
    l.append(k)
t=tuple(l)
ts=0
s=0
for i in t:
    s+=1
    ts+=i
print()
print("The length of the tuple is: %s"%s)
print("The sum of the tuple is: %s"%ts)
    
