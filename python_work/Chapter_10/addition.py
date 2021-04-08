def addition(num1, num2) :
    """Simple function to add 2 numbers while error checking"""
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("Please enter numbers values.")
    else:
        print(answer)


while True:
    print("Enter 'q' to exist the program.")
    num1 = input("Enter your first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter your second number: ")
    if num2 == 'q':
        break
    addition(num1,num2)
