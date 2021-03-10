# This program says hello ans ask for my name 

print('Hello World!')

print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ' + str(len(myName)))
#print(len(myName))

print('What is your age?') # ask for their age
#input function always returns a string 
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
