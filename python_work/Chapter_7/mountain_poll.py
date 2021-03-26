# declaring the dictionary 
responses = {}

#Set the flag to indicate that polling is active.
polling_active = True

while polling_active:
    # prompt for the person's name and responce.
    name = input("\nWhat is your name? ")
    responce = input("Which mountain would you like to climb someday? ")

    #store the responce in the dictionary
    responses[name] = responce

    #find out if anyone else if going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
# Polling is complete. Show the results. 
print("\n--- Poll Results ---") 
for name, responce in responses.items():
    print(f"{name} would like to climb {responce}.")