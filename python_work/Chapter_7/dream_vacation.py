responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where is your dream vacation at? ")

    responses[name] = response

    ask = input("would you like to let another person respond? (yes/no) :")
    if ask == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()}'s, dream vacation is at {response.title()}.")