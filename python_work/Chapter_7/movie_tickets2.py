# while loop that uses active variable
prompt = "What is your age? "
status = True

while status:
    age = input(prompt)

    if age != 'exit':
        age = int(age)
        if age < 3 :
            print("The price for your ticket is free, Enjoy!")
        elif age <= 12: 
            print("The price for your ticket is $10.")
        else:
            print("The price for your ticket is $15.")
    else:
        status = False