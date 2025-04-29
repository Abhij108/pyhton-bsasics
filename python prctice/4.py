# #Develop a program that asks the user for a sentence and uses a
# for loop to count and display the number of vowels (a, e, i, o, u)
# in the sentence.
sentence = input("enter a sentence:")
vowel = 'aeiou'
count = 0

for i in sentence:
    if i in vowel:
        count +=1
print(count)