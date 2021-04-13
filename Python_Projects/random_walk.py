from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # all walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate the all points in the walk"""

        #keep taking steps until the walk reaches a desired length]
        while len(self.x_values) < self.num_points:

            #decide which direction to go and how far to go in that direction.
            x_step = self.get_step()
            y_step = self.get_step()

            # reject the moves that go nowhere 
            if x_step == 0 and y_step == 0:
                continue

            # caculate the new position 
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Calculate the step in either the x or y direction"""
        # a stands for axis, which referes to either x or y
        a_direction = choice([1, -1])
        a_distance = choice([0,1,2,3,4])
        a_step = a_direction * a_distance
        return a_step


