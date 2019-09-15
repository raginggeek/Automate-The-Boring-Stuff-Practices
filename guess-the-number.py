# this is a guess the number game

import random

# get the users name
print('Hello, what is your name?')
name = input()

# prime the number
secretNumber = random.randint(1, 20)

# welcome the user to the game
print('Well, ' + name + " I am thinking of a number between 1 and 20.")

guess = 0
guessesTaken = 0
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Too low.')
    elif guess > secretNumber:
        print('Too high')
    else:
        break  # correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
