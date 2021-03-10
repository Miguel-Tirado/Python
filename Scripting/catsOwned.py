print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4: 
        print('That is a lot of cats.')
    elif int(numCats) <= 0: 
        print('you dont have any cats.')
    else: 
        print('That is not that many cats.')
except ValueError: 
    print('You did not entor a number.')


print('Hello.')