
file_path = 'text_files/pi_digits.txt'

# notice here that i can access the context of the pi file by storing it into the list lines 
# then reading of the list in the for loop
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())