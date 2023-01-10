a=int(input("enter a number"))
b=int(input("enter another number"))
def calculator(**name):
    x = str(input("what you want sum/diff/mul/div :"))
    print("result of "+name[x])
calculator(sum =str(a+b),diff= str( a-b),mul=str(a*b),div =str(a/b))

