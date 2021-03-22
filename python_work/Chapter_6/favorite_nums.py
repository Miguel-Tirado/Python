fav_numbers = {
    'miguel' : [8,7,22,4],
    'bob' : [3,7,12,88,2],
    'richard': [25, 14, 99, 26],
}

for person, numbers in fav_numbers.items():
    print(f"{person.title()}'s favorite numbers are the following:")
    for number in numbers:
        print(f"   {number}")