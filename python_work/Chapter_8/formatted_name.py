def get_formatted_name(first_name, last_name, middle_name=''):
    """return full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:  
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")

    responce = input("would you like to continue -> (yes/no): ")
    if responce == 'no':
        break
    