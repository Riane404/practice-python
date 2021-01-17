i=2
s=1
j=0
k=0
while(s<=20):
    k=0
    for j in range(2,i):
        if (i%j)==0:
            k+=1
            break
    if k==0:
        print(i,end=" ")
        s+=1
    else:
        pass

    i+=1
print("are the first 20 prime numbers")
    
        
