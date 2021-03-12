guesst = ['richard','jesus','sam']

for i in range(len(guesst)):
    print(f"Hello {guesst[i]}, I am inviting your to dinner.")
print(f"Unfortunately {guesst[0]}, can not make it to dinner.")
guesst.remove('richard')
guesst.insert(0, 'Javier')
for i in range(len(guesst)):
    print(f"The new list of people im inviting starts with {guesst[i]}.")
print("I found a bigger table and more guest to join.")
guesst.insert(0,'Santiago')
guesst.insert(1, 'Ramya')
guesst.append('Clara')
for i in range(len(guesst)):
    print(f"the new list start with {guesst[i].title()}.")
print("It looks like i can only invite 2 people since my new table wont make it on time")
for i in range(0,(len(guesst)-2)):
    denied = guesst.pop()
    print(f"Im sorry {denied}, but we cant invite you anymore to dinner.")
for i in range(len(guesst)):
    print(f"hello {guesst[i].title()}, welcome to the dinner later.")
del guesst[0]
del guesst[0]
print(guesst)

