#by using functions i am implementig the calculator
def ADD(x,y):
    return x+y

def Subtract(x,y):
    return x-y



def Mul(x,y):
    return x*y

def div(x,y):
    return x/y


def mod_div(x,y):
    return x%y

x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
opt=input("Enter the choice")

if opt=="+":
    res1=ADD(x,y)
    print(res1)
elif opt=="-":
    res2=Subtract(x,y)
    print(res2)
elif opt=="*":
    res3=Mul(x,y)
    print(res3)
elif opt=="/":
    res4=div(x,y)
    print(res4)
else:
    res5=mod_div(x,y)
    print(res5)




