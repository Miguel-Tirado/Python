pet_0 = {
    'animal' : 'dog',
    'breed' : 'husky',
    'name' : 'rex',
    'owner' : 'miguel',
    'age' : 6
}

pet_1 = {
    'animal' : 'bird',
    'breed' : 'parakeet',
    'name' : 'lola',
    'owner' : 'sarah',
    'age' : 4
}

pet_2 = {
    'animal' : 'lizard',
    'breed' : 'skink',
    'name' : 'larry',
    'owner' : 'robert',
    'age' : 3
}

pets = [pet_0,pet_1,pet_2]

for pet in pets:
    animal = pet['animal']
    breed = pet['breed']
    name = pet['name']
    owner = pet['owner']
    age = pet['age']

    print(f"my name is {name} and i am a {breed} which is a type of {animal}."
          f" I am {age} years old and my owners name is {owner}.")