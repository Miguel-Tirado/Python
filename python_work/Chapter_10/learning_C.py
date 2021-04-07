file_path = 'learning_python.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python','C'))
