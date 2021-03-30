# creating a simple function and testing it
def greet_user():
    """Display a simple greeting"""
    print("Hello!")

def greet_name(name):
    """Display a greeting while passing in a parameter"""
    print(f"Hello, {name.title()}.")

greet_user()
greet_name("miguel")
