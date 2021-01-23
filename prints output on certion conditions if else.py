n = int(input("Enter the number: "))
if n%2!=0:
    print("Weird")
else:
    if n>20:
        print("Not Weird")
    if n in range(2,6):
        print("Not Weird")
    if n in range(6,21):
        print("Weird")

