i=5
s=0
t=0
for j in range(0,i):
    s=i-j
    t=0
    for q in range(0,s-1):
        print("_",end="")
        t+=1
    
    for t in range(s+1,i+2):
        print("* ",end="")
    print()


