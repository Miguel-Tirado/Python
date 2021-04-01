# passing an arbitrary amount of arguments into a function
# also mixing positional with arbitrary
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers', 'extra cheese')
