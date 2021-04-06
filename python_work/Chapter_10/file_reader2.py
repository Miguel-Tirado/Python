file_path = 'text_files/pi_digits.txt'
with open(file_path) as file_object:
    # to remove the newline character we must use rstrip()
    for line in file_object:
        print(line.rstrip())