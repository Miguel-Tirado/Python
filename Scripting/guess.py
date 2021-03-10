# this is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)
# Note that python uses function level scoping thus allowing us to use the variable guess later
# i added the guess equal to none here to give me a clue but note its not necessary for this to work 
# guess = None

for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber :
        print('youre guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this condidition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessTaken) + ' guesses')
else:
    print('Nope. the number i was thinkong of was ' + str(secretNumber))

