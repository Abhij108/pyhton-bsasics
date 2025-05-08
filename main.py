# import os    # rename files with the help of os module
# files = os.listdir("cluttred")          # listv the files present in cluttred folder
# i = 1

# for file in files:
#     if file.endswith(".png"):               # find png files:
#         os.rename(f"cluttred/{file}", f"cluttred/{i}.png")      # os method to rename files :
#         i = i+1
#     else:
#         pass

n = int(input("enter a numbeerr"))
m = int(input("enter a number"))

for numrow in range(n):
    for numcol in range(m):
        print(numcol+1, end=" ")
    print(" ")