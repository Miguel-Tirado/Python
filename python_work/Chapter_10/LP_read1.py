file_path = 'learning_python.txt'

with open(file_path) as file_object:
    lines = file_object.read()

for i in range(3):
    print(f"{lines}\n")