prompt = "Enter the toppings your would like on your pizza: "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(f"adding {message} to pizza.") 