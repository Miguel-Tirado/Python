favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

# to use the dictioary, given the name of a person who took the pool

lanaguage = favorite_languages['sarah'].title()
print(f"Sarah's favorite langauge is {lanaguage}.\n")

# adding a for loop to iterate over the dictionary 
for name,langauge in favorite_languages.items():
    print(f"{name.title()}'s favorite langauge is {lanaguage.title()}.")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")