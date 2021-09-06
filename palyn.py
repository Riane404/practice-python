i=int(input("Enter the number: "))
c=i
j=0
k=0
print()
while(i>0):
    j=(i%10)
    k=(k*10)+j
    i=i//10
    
if k==c:
    print("It is a palyndrom")

else:
    print("It is not a palyndrom")

