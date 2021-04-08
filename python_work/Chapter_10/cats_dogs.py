def read_files(file_name):
    """Reads the files and prints them out"""
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry {file_name} was not found")
        pass
    else:
        print(contents)

file_names = ['text_files/cats.txt','dogs.txt']
for file_name in file_names:
    read_files(file_name)