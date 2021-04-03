class Car:
    # Car is a super class or parent class 

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer} miles on it.")
    
    def upate_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You cant roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer += miles

class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles."""
    # ElectricCar is a sub class of Car

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla','model s','2020')
print(my_tesla.get_descriptive_name())