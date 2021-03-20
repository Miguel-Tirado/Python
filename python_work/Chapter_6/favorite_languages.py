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

print("")

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\nIn order list")

# print a sorted dictionary 
print("\nprinting in a sorted order")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# looping through all values in a dictionary
print("\nThe following languages have been mentioned:")
for langauge in set(favorite_languages.values()):
    print(langauge.title())

# set is a collection of items that must be unique 
# when you see braces with no key values pairs ('jen' : 'python') is prob a set
print("here is a set of different languages")
lanaguages = {'python','c','java','ruby'}
print(lanaguages)
