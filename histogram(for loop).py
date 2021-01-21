i=input("Enter the values: ")
j=i.split(" ")
print(i)
for k in j:
    k=int(k)
    for l in range(0,k):
        print("██",end="")
    print()
