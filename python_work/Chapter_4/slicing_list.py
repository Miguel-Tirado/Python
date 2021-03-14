players = ['charles','martina','michael','florence','eli']
# notice that python always starts and ends one index before when using slices 
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
# copying a list 
my_foods = ['pizza', 'falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('Cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy fiend's favorite foods are:")
print(friend_foods)