def add(a,b):
    add = a+b

    return add
def diff(a,b):
    diff = a-b

    return diff
def mul(a,b):
    mul = a*b
    return mul
def div(a,b):
    div = a/b
    return div

a= int(input("enter a number"))
b= int(input("enter a number "))

print("for additon=1 /n substraction=2 /n multiplication=3 /n division=4")
n = int(input("select from above"))

if n==1:
    print("sum of two numbers is",add(a,b))
elif n==2:
    print("substraction of numbers is :",diff(a,b))
elif n==3:
    print("multiplication of number is :",mul(a,b))
elif n==4:
    print("division of numbers is :",div(a,b))




