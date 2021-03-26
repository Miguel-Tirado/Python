# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# adding a while loop to iterate as many times until the user wants to quit
new_message = ''
while new_message != 'quit':
    new_message = input(prompt)
    if new_message != 'quit':   
        print(new_message)