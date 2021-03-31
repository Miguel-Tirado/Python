def describe_city(city_name, country = 'United States of America'):
    print(f"{city_name.title()} is in {country.title()}.")

describe_city('sacramento')
describe_city('tokiyo','japan')
describe_city(city_name='london',country='new england')