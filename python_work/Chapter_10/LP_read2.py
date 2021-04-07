file_path = 'learning_python.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()
    for i in range(3):
        for line in lines:
            print(line.strip())
        print('')
