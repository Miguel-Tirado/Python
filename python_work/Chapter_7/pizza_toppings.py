prompt = "Enter the toppings your would like on your pizza: "
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"adding {message} to pizza.") 