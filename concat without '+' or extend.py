i=int(input("Enter the number of values in the list: "))
l1=list()
l3=list()
for j in range(0,i):
    lv1=input("Enter the value to be added: ")
    l1.append(lv1)

i=int(input("Enter the number of values in the 2nd list: "))
l2=list()
for j in range(0,i):
    lv2=input("Enter the value to be added: ")
    l2.append(lv2)

print()

for i in l1:
    l3.append(i)    
for i in l2:
    l3.append(i)
print(l3)
