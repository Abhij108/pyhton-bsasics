# factorial of numbers 

def fact(n):
    '''this is a program for factorial:'''
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact.__doc__)
print(fact(4))
print(fact(3))
print(fact(19))
print(fact(8))

# fibonaccin series and doc-string example:

a = 0
b = 1
c = a+b

def fibbo(n):
        '''this is a program for fibbonnaci series:'''

        if n <0:
            return ("incorrect value :")
        elif n==0:
            return 0 
        elif n==1 or n==2:
            return 1
        else:
           
            return fibbo(n-1) + fibbo(n-2)
    
print(fibbo.__doc__)
print(fibbo(9))
print(fibbo(5))
print(fibbo(3))

# f-string :
name = "abhi"
country = "India"
txt = f"Hi my name is {name} and I am from {country}"
print(txt)