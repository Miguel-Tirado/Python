alien_o = {'color': 'green', 'speed' : 'slow'}
# print(alien_o['points'])
# using the get method to set a default value for points if it doesnt exist in the dictionary
point_value = alien_o.get('points','No point value assigned.')
print(point_value)