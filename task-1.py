#Creating command line calculator supporting basic operations

def add(x,y):
    print(x+y)

def subtract(x,y):
    print(x-y) 

def multiply(x,y):
    print(x*y) 
def divide(x,y):
    print(x/y) 
while(True):
    ch=int(input("Enter Your Choice Of Operation 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Exit"))
    if ch==1:
        x=int(input("Enter first number..."))
        y=int(input("Enter second number..."))
        add(x,y)
    elif ch==2:
        x=int(input("Enter first number..."))
        y=int(input("Enter second number..."))
        subtract(x,y)
    elif ch==3:
        x=int(input("Enter first number..."))
        y=int(input("Enter second number..."))
        multiply(x,y)
    elif ch==4:
        x=int(input("Enter first number..."))
        y=int(input("Enter second number..."))
        divide(x,y)
    else:
        exit()

