import time 
timestamp  = time.strftime('%H : %M : %S')
print(timestamp)
hours = int(time.strftime('%H'))
print(hours)

if(hours>=00 and hours<12):
    print("Good Morning Sir :")
elif(hours>=12 and hours < 20):
    print("Good evening sir")
else:
    print("Good night sir ")