# progaram to print the even number int the list 

l = [1,2,3,4,5,6,7,8,9,10,12,13]
for i in l:
    if i%2 ==0:
        print(i)

# progaram for print odd number and skip even number

for num in l:
    if num%2==0:
        continue
    print(num)

#Print numbers but skip even numbers and stop if numbergreater than 10 is found

for i in l:
    if i %2 ==0:
        continue
    elif i>10:
        print("number is greater than 10" )
        break
    print(i)
