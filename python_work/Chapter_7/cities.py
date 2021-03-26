
prompt = "\nPlease enter the name of a city you visited: "
prompt += "\n(Enter 'quit' when you are finished. "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else :
        print(f"Id love to go to {message.title()}.")