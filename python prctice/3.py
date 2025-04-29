# Create a script that counts the number of vowels in a given string.
def vowel(string):
    vow = 'aeiou'
    count = 0

    for char in string.lower():
        if char in vow:
            count +=1

    return count
        
print(vowel('helloworld'))

