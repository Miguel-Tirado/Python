class Dog:
    """A simple attempt to model a dog"""
    # Note that attributes is 

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """simulate a dog sitting in responcse to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in responce to a command"""
        print(f"{self.name} rolled over!")

# creating instances of the class Dog
my_dog = Dog('rex',3)
your_dog = Dog('peluchin',7)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog's is {my_dog.age} years")
my_dog.sit()
my_dog.roll_over()

print(f"\nMy dog's name is {your_dog.name.title()}.")
print(f"My dog's is {your_dog.age} years")
your_dog.sit()
your_dog.roll_over()