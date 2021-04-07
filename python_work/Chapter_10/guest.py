file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
    name = input("Enter your name here: ")
    file_object.write(name)