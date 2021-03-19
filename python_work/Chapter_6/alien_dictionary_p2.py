# traking down the speed of a alien that can move at different speeds 
alien_o = {'x_position': 0, 'y_position' : 25, 'speed': 'medium'}
print(f"original position: {alien_o['x_position']}")

if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else :
    x_increment = 3

alien_o['x_position'] = alien_o['x_position'] + x_increment

print(f"new position: {alien_o['x_position']}")

