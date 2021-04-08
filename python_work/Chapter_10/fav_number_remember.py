import json

filename = 'fav_num.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number,f)
        print(f"Well remember your favorite number when you come back.")
else:
    print(f"Your favorite number is {number}.")