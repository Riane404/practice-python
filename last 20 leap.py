s=1
i=int(input("What year is it: "))
while (s<=20):
    if (i%4)==0:
        if (i%100)==0:
            if(i%400)==0:
                print(i,end=" ")
                s+=1
            else:
                pass

        
        else:
            print(i,end=" ")
            s+=1

    else:
       pass
    i-=1
print("are the last 20 leap years")

    
