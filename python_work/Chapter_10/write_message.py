file_name = 'programming.txt'

# the possible modes to open a file are 
# modes:       'r'   Read (Default) mode
# modes:       'w'   Write mode
# modes:       'a'   Append mode
# modes:       'r+'  Read and write mode 
with open(file_name,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")