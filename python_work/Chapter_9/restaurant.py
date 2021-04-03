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


restaurant1 = Restaurant('culichi town','mexican')
restaurant2 = Restaurant('Chick fil A','american')
restaurant3 = Restaurant('YD tofu house','korean')
restaurant = Restaurant('taco bell', 'mexican')

# restaurant.number_served = 4
# print(restaurant.number_served)

restaurant.set_number_served(20)
print(f"The number of served people at {restaurant.restaurant_name} is {restaurant.number_served}")
restaurant.increment_numbers_served(10)
print(f"A total of {restaurant.number_served} people were served today.")

print(f"\nMy favorite restaurant is {restaurant1.restaurant_name.title()}.")
print(f"They serve {restaurant1.cuisine_type} food.\n")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#restaurant1.open_restaurant()
#restaurant1.describe_restaurant()
