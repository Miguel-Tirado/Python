import turtle
import time

# Constant Values for window size
WIDTH, HEIGHT = 500, 500

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10)-> ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try Again!")
            # This continue is used to skip the bottom block of code ->
            # if the user did not enter a digit value then racers
            # would have not been converted to a int value, which can cause problems
            # with the comparision down below.
            continue

        # racers at this point is not a number or integer data type 
        # so this conditional statement should work.
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try Again!")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
init_turtle()

