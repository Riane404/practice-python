i=1
j=1
s=1
for i in range(1,11,1):
    j=1
    for s in range(i,0,-1):
        j=j*s
    print(i,"factorial is",j)

