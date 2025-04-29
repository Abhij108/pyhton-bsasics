#Write a program that checks if a given number is even or odd
# using conditional statements.
while True:
    num = int(input("enter a number"))
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        break
