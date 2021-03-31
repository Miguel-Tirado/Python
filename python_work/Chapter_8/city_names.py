def city_country(city, country):
    place = f"{city.title()} {country.title()}"
    return place

location = city_country('sacramento','United State of America')
print(location)
location = city_country('tokiyo','japan')
print(location)
location = city_country('madrid','spain')
print(location)