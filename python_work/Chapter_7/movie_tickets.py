# simple porgram that ask users for their age and then tells them the cost of their ticket
prompt = "What is your age? "

age = ''
while age != 'exit':
    age = input(prompt)
    if age != 'exit':
        age = int(age)
        if age < 3 :
            print("The price for your ticket is free, Enjoy!")
        elif age <= 12: 
            print("The price for your ticket is $10.")
        else:
            print("The price for your ticket is $15.")