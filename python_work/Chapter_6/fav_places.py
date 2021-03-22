favorite_places = {
    'miguel' : ['san fransico', 'japan', 'spain'],
    'jesus' : ['los angelos', 'germany', 'brazil'],
    'dianna' : ['houston', 'mexico'],
}

for name, locations in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for location in locations:
        print(f"\t{location.title()}")