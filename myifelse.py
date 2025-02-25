# to check the certain values and to check conditions use conditional statement:
# they are :
'''
1. if 
2.if - else
3. elif 
4. nested if-else'''

# we have to check the age of driving :

a = int(input("Enter your age :"))
if(a>=18):
    print("you can drive ")
else :
    print("you cannot drive ")

# conditional statement with elif

num = int(input("Enter number: "))

if(num < 0 ):
    print("number is negative ")
elif(num > 0 ):
    print("number is positive")
else:
    print("thankyou")


# Nested if_else statement
num1 = int(input("Enter number: "))

if(num1 < 0 ):
    print("number is negative ")
elif(num1 > 0 ):
    if (num1>1 and num1 <10):
        print("Number is between 1-10")
    elif(num1>10 and num1<20):
        print("Number is between 10-20")
    else:
        print("number is grester than 20 ")
else:
    print("thankyou")

