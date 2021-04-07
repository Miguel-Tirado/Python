file_name = 'guest_book.txt'

while True:
    name = input("Please enter your name here: ")
    if name == 'quit':
        break
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(f"{name}\n")
        print(f"Hello {name}, you've been added to the guest book.")