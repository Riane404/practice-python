print("Guide:'+'=addition,'-'=substract,'*'=multiply,'/'=divide")
print("'ch'= change values,'end'=End the calculator,'help'=display the Guide")
l1=list()
f=""
i=float(input("Enter the first val: "))
j=float(input("Enter the second val: "))

def help():
    print("Guide:'+'=addition,'-'=substract,'*'=multiply,'/'=divide")
    print("'ch'= change values,'end'=End the calculator")

def fun():
    f1=input("What do you want to do: ")
    return(f1)

def add(i,j):
    a=i+j
    print(a,"is the addition")

def sub(i,j):
    s=i-j
    print(s,"is the substraction")

def div(i,j):
    d=i/j
    print(d,"is the division")

def mul(i,j):
    m=i*j
    print(m,"is the multiplication")

def num1():
    i1=float(input("Enter the first val: "))
    return(i1)

def num2():
    j1=float(input("Enter the second val: "))
    return(j1)
    

while f!="end":
    while f!="end":
        f=(fun())
        if f=="+":
            add(i,j)

        elif f=="-":
            sub(i,j)

        elif f=="*":
            mul(i,j)

        elif f=="/":
            div(i,j)

        elif f=="help":
            help()
        
        elif f=="chg":
            i=num1()
            j=num2()

        elif f=="end":
            pass
        
        else:
            print("Enter a valid operator and try again. Type'help' for the guide.")
            
        print()

    


