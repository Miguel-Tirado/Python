cities = {
    'sacramento' : {
        'country' : 'united state of america',
        'population' : 68000000,
        'fact' : 'city of trees',
    },
    'san fransisco' : {
        'country' : 'united state of america',
        'population' : 87000000,
        'fact' : 'city of tech companies',
    },
    'tokiyo' : {
        'country' : 'japan',
        'population' : 673302393,
        'fact' : 'biggest city in japan',
    }
}

for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f"{city.title()} is in {country.title()}.")
    print(f"   It has a population of {population}.")
    print(f"   Its the {fact}.")
 
    