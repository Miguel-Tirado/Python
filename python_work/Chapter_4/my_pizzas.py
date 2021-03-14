pizzas = ['Hawaian','Perporni','Stuffed crust']
friend_pizzas = pizzas[:]

pizzas.append('meat lovers')
friend_pizzas.append('cheese')

print("My favorite pizza are: ")
for pizza in pizzas:
    print(pizza)
print("My friends favortie pizza are: ")
for pizza in friend_pizzas:
    print(pizza)