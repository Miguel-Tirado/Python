prompt = "Enter the toppings your would like on your pizza: "

message = ''

while message != 'quit':
    message = input(prompt)
    print(f"adding {message} to pizza.")