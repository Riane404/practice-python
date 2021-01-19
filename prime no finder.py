i=int(input("Enter the value: "))
k=0
l=0
print()
print(i,"is divisible by",end=" ")
for j in range(2,i,1):
    if i%j==0:
        k+=1
        print(j,end=",")
        #break
            
if k==0:
    print("only itself and 1 therefore",i,"is a prime number")

else:
    print("therefore",i,"is not a prime number")
