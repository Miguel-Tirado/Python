import turtle
import time
import random

# Constant Values for window size
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

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

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]



def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    # enumerate gives us both the index and the values of items in the list
    # note racers by default point right, thus we need to shift the position left by 90
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # set pos
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers] # this slice gives us a new random list of colors with the number of racers given

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)