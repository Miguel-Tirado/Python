fav_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    'miguel' : ['Java'],
}

# looping through the key value pairs in the dictionary in the first loop
# 2nd loop we are looping through the items inside the list that are our values of the dic
for name, langauges in fav_languages.items():
    if len(langauges) > 1:
        print(f"\n{name.title()}'s favorite languages are:") 
        for langauge in langauges:
            print(f"\t{langauge.title()}")
    else: 
        print(f"\n{name.title()}'s favorite language is", end='')
        for langauge in langauges:
            print(f" {langauge.title()}")