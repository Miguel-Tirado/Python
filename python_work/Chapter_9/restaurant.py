class Restaurant:
    """Simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """prints 2 piece of info about the restaurant"""
        print(f"Welcome to {self.restaurant_name}.")
        print(f"We serve {self.cuisine_type} food.")
    
    def open_restaurant(self):
        """prints that the restaurant is open"""
        print("We are open!")
    
    def set_number_served(self, people):
        self.number_served = people
    
    def increment_numbers_served(self, amount):
        self.number_served += amount
