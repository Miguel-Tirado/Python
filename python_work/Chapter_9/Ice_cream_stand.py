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

class IceCreamStand(Restaurant):
    """Simple attempt to model a ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of parent class
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def list_flavors(self):
        """prints our all the available flavors"""
        for flavor in self.flavors:
            print(f"current flavor: {flavor}")

ice_cream_shop1 = IceCreamStand('gunthers','american')
ice_cream_shop1.flavors = ['choclate','vanilla','strawberry','mango']
ice_cream_shop1.list_flavors()
    

