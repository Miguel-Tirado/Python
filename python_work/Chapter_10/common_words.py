def count_words(file_name):
    """Count the approximate number of words in a file"""
    # in order to fail silently we can replace the print statement inside the except block
    # with a pass statement which tells python to do nothing for that block of code
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {file_name} does not exist.")
        pass
    else:
        # count the approximate number of words in the file.
        words = contents.lower().count('the ')
        # num_words = len(words)
        print(f"The file {file_name} uses the word 'the', this amount of time {words}.")

file_names = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for file_name in file_names:
    count_words(file_name)