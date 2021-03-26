# note here I am using a flag to control when the while loop stops
# if the use type's quit the loop stop with the flag active being set to false
# this is a version of parrot.py file I made using flags

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "


active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)