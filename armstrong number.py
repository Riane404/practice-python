i=int(input("Enter the number: "))
c=i
j=0
s=0
print()
while(i>0):
    j=(i%10)
    i=i//10
    s+=j**3

if s==c:
    print("It is an armstrong number")

else:
    print("It is not an armstrong number")

   

