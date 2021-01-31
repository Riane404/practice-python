def factorial(n):
    s=1
    for k in range(1,n+1):
        s=s*k  
    print(s)  

n=int(input())
factorial(n)
