# creating 3 different alien dictionaries 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# creating a list of dictionaries 
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens
more_aliens = []

# Make 30 gree aliens
for alien_num in range(30):
    new_alien = {'color' : 'green', 'points': 5}
    more_aliens.append(new_alien)

# show the first 10 aliens 
for alien in more_aliens[:10]:
    print(alien)
print("...")

#Show how many aliens have been created.
print(f"there number of aliens: {len(more_aliens)}")