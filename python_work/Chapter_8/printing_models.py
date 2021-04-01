
import printing_functions

# Start with some designs that need to be printed 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

unprinted_reverse = unprinted_designs[::-1]
print(unprinted_reverse)
print(unprinted_designs)

printing_functions.print_models(unprinted_designs,completed_models)
printing_functions.show_completed_models(completed_models)