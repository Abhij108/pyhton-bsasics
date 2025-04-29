#Create a program that prompts the user to enter their age and
#checks if they are a child (0-12 years), a teenager (13-19 years),
# or an adult (20 years and older).
def check_age(n):
    if n<=12:
        print("child")
    elif n>=13 and n<=19:
        print("teenager")
    else:
        print("adult")

if __name__ == '__main__':
    n = int(input("enter your age:"))
    check_age(n)