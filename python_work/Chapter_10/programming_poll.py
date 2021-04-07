file_name = 'poll.txt'

while True:
    responce = input("Why do you like programming?\n")
    if responce == 'quit':
        print("Your responce has been recorded.")
        break
    else:
        with open(file_name, 'a') as file_object:
            #file_object.write(responce + '\n')
            file_object.write(f"{responce}\n")
        