i=int(input("enter the length of * needed:"))
k=0
s=0
t=0
for j in range(0,i):
    s=i-j
    k=s
    for c in range(0,s):
        print("* ",end="")
   
    print()
    while ((k>=s)and(k<=i)):
        print("_" ,end="")
        k+=1

    
    
