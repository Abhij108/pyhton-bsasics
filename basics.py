# how to define variable in python :

a = 1 # a is integer valued variable :
print(a)

b = "abhijeet" # value of b is str :
print(b)

f = 3.141
print(f)

# to find the types of variable or data :

print(type(a))
print(type(b))

# type conversion / type casting  :
c = float(a)
print(c)
s = int(f)
print(s)

''' data types in python
1. int = it is for integer type value 
2. float = int is used to define floating values (1.2,3.243 , 3.41 etc)
3.bool =  it is boolean data type tells true or false 
4. list = list in python is collection of similar or different type of data which is mutable in nature .
5. tuple = tuple is same as list but it can not be mutable 
6. dictionary = dictinory is a mapping data type which contains key value 
'''
int = 123 
print(int)

float = 3.141
print(float)

bool = True 
print(bool)

list = [1,2,3,["apple", "banana", "mango"] , ["horse","goat","monkey"]]
print(list)

tuple = (1,2,3, "apple","monkey")
print(tuple)

dict = {int:[1,2,3,4,5]}
print(dict)

# operatores :
# WAP to ADD TWO numbers in python :

num1 = 144
num2 = 546
print("addition is :", num1+num2)
print("substraction  is :", num1-num2)
print("multiplication is :", num1*num2)
print("division is :", num1/num2)
print("floor devision is :", num1//num2)
print("remainder or modulo is :", num1%num2)
print("exponential :", num1 ** num2)



# taking of user input 
# in python use input function to take input from the user 

#name = input("enter your name :")
#print(name )


# STRINGS : anything enclose in double or single qutation is considered string :

str = "hi my name is abhijeet verma \n iam a btech student :"
print(str )
print(len(str))  # len() function is used to find the length of  string. String is like an array of character 
print(str[0:2])   # slicing of string 
