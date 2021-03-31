def make_shirt(size = 'large', shirt_msg = 'I love python'):
    """prints a msg about the shirt size and what it says"""
    print(f"The shirt size is {size} and the message on the shirt says {shirt_msg.title()}.")

make_shirt('small','live life to the fullest')
make_shirt(shirt_msg='the sun will rise again', size='medium')
make_shirt()
make_shirt('medium')
make_shirt('small','I love c')