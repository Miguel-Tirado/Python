def make_sandwhich(*ingrediants):
    """prints a summary of the sandwhich ordered"""
    print("\nI'll make you a mean samich")
    for ingrediant in ingrediants:
        print(f"Adding {ingrediant} to your sandwhich.")
    print("\nYour sandwhich is ready boss.")

make_sandwhich('roast beef','lettuce','tomatoe','mayo')
make_sandwhich('bacon','lettuce','tomatoe')
make_sandwhich('ham')