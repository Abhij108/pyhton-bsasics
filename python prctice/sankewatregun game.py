import random
def check(user,com):

    if user== com :
        return 0
    if user==0 and com ==1:
        return 1
    if user == 1 and com ==2:
        return 1
    if user == 2 and com == 0:
        return 1 
   
    return -1


user = int(input("0-snake,1-water,2-gun"))
com = random.randint(0,2)

score = check(user,com)
print('user:',user)
print('computer:',com)

if score == 0:
    print("Draw")
elif score==1:
    print("you won")
else:
    print("you lose")


