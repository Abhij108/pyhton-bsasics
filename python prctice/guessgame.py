# Number Guessing Game
# Task: Write a simple number guessing game using Python. The program
# should generate a random number between 1 and 100, and prompt the user
# to guess the number.
import random

def guess():
    number = random.randint(1,100)
    
    attempts = 0

    while True:
        guessnum = int(input("guess number between 1to100:"))
        attempts +=1
        if guessnum > number:
            print("number is to high")
        elif guessnum < number:
            print("guessnum is to low ")
        else:
            print("congratulation")
            break

if __name__ == '__main__':
    guess()
