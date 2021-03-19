alien_o = {'color':'green','points':5}

print(alien_o['color'])
print(alien_o['points'])

# We can look up how many points a player earns when shooting down a alien by using:
new_points = alien_o['points']
print(f"You just earned {alien_o['points']} points!")

# adding to the x and y position of the alien onto the dictionary
alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)

# delcaring an empty dictionary
alien_p = {}

alien_p['color'] = 'yellow'
alien_p['points'] = 10
print(alien_p)
# modifying values in a dictionary
alien_p['color'] = 'red'
print(f"The alien_p is now {alien_p['color']}.")

# removing key value pairs from a dictionary
del alien_o['points']
print(alien_o)