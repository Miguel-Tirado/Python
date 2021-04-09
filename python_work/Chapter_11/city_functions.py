def get_city_function(city,country, population=''):
    """Generate a neatly formatted location"""
    place = f"{city}, {country} - population {population}"
    return place.title()