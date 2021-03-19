# note this method of opening and closing the file is not safe
f = open("simple.txt",'r')
f.close()

# the format to open a file is:
# f = open("test.txt", mode='r', encoding='utf-8')
# mode can be 'r' read only
# modes:      'w' write only 
# modes:      'a' opens a file for appending at the end of the file w/o truncating it
# modes:      't' opens in text mode (default)
# modes:      'b' Opens in binary mode 
# modes:      '+' opens a file for updating(reading and writing)
# f = open("simple.txt")  the same as to 'r' or 'rt'

# when working with files in text mode, its recommended to specify the econding type,
# since its different depending on the OS such as window and linux
f = open("simple.txt", encoding= 'utf-8')
f.close()

# a safer way to close is 
try:
    f = open("simple.txt", encoding='utf-8')
finally:
   f.close()

# the best way to close is
# note that the close() is done internally when using the with keyword
with open("simple.txt", encoding= 'utf-8') as f:
    # preform file operations
    print(f.read())
    # read a file line by line
    for line in f:
        print(line, end = '')

# note that the write() create a new file anmed write.txt in the current directory if does not exist
# if it does exist, it is overwritten
with open("write.txt",'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
