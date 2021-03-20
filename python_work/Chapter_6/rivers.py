rivers = {
    'american' : "united state's of america",
    'sacramento' : "united state's of america",
    'rio grande' : "mexico",
}

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country}." )

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe follwing countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")