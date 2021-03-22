person_a = {
    'first_name' : 'miguel',
    'last_name' : 'tirado',
    'age' : 22,
    'city' : 'sacramento'
}

person_b = {
    'first_name' : 'jesus',
    'last_name' : 'nunez',
    'age' : 26,
    'city' : 'sacramento'
}

person_c = {
    'first_name' : 'Jonh',
    'last_name' : 'Doe',
    'age' : 28,
    'city' : 'los angelos'
}

persons = [person_a,person_b,person_c]

for person in persons:
    first = person['first_name']
    last = person['last_name']
    age = person['age']
    city = person['city']
    print(f"{first} {last} of {city}, is age {age}.")