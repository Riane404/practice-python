print('hello world')
print()
print('enter a value')
i=int(input())
print(i)

print()
print()

k=1
s=1
o=0
print(k,s,end=',')
for j in range(2,i):
    o=k+s
    print(o,end=',')
    s=k
    k=o
    
print()

a=int(input('enter the multiplication table required:'))
print()
b=int(input('enter how many multiplications required: '))

print()
print()

for i in range(1,b+1):
    print(a,' * ',i,' = ',a*i)

    
    
