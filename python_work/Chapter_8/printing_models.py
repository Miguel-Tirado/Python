def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        # Simulate printing each design, until none are left
        # move each design to completed_models after printing 
        current_design = unprinted_designs.pop()

        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    #Display all completed models.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Start with some designs that need to be printed 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

unprinted_reverse = unprinted_designs[::-1]
print(unprinted_reverse)
print(unprinted_designs)

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)