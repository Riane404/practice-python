i=input("Enter the values : ")
l=i.replace(",",":")
l=l.split(":")
s=0
sv=0
mv=0
t=2
m=0
for i in l:  
    c=l.index(i)
    if c%2!=0 :
        sv=int(i)
        s+=sv
    else:
        mv=int(i)
        m+=mv

ts=s/60
tt=ts+m
h=tt/60

print("The total time required is:",h,"hours")

   


