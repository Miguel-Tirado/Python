# creating a simple function and testing it
def greet_user():
    """Display a simple greeting"""
    print("Hello!")

def greet_name(name):
    """Display a greeting while passing in a parameter"""
    # note name here is a parameter
    print(f"Hello, {name.title()}.")

greet_user()
# note here that "miguel" is the argument
greet_name("miguel")
