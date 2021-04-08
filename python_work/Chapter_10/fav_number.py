import json

fav_num = input("what is your favorite number? ")

filename = "fav_nums.json"
with open(filename, 'w') as f:
    json.dump(int(fav_num), f)
