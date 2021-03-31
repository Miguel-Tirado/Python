def describe_pet(pet_name, animal_type = 'dog'):
    """Display info about the pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

def des_more_pet(pet_name, animal_type = 'cat'):
    """Display info about the pet with a default value parameter"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")



# note this is using positional arguments 
# order madders when providing arguments
describe_pet("hamster",'harry')
# This is using keyword arguments
# order does not madder when providing arguments
describe_pet(animal_type='dog', pet_name='rex')
describe_pet(pet_name='mango', animal_type='bird')
# this is using a default value for animal type
describe_pet(pet_name='wille')
describe_pet('willie')
