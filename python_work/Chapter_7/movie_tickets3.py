# while loop that uses a a break statment 
prompt = "What is your age? "

while True:
    msg = input(prompt)
    if msg == 'quit':
        break
    
    msg = int(msg)
    if msg < 3 :
        print("The price for your ticket is free, Enjoy!")
    elif msg <= 12: 
        print("The price for your ticket is $10.")
    else:
            print("The price for your ticket is $15.")