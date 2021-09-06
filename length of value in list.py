i=int(input("Enter the number of values to be entered: "))
l=list()
c=0
q=0
q1=0
for j in range(0,i):
    e=input("Enter the values: ")
    l.append(e)

for i in l:
    q=len(i)
    
    if q1<q:
        c=l.index(i)
        q1=len(i)
    
print("The longest value is",l[c])



