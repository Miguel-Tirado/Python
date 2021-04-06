from random import randint

class Dice:
    """Simple attempt at modeling a dice"""
    def __init__(self,sides=6):
        self.sides = sides

    def roll_dice(self):
        rand_num = randint(1,self.sides)
        print(f"You rolled: {rand_num}")

dice1 = Dice()
dice2 = Dice(10)
for i in range(10):
    dice1.roll_dice()
print("---------10 sided dice----------")
for j in range(10):
    dice2.roll_dice()

        