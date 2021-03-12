# Simple program to print greetings of my list of friends 
names = ['jesus','Sam','Javier','Ramya','Clara','Santiago']
for i in range(len(names)):
    print("Method1")
    print(f"Hello {names[i]}, how was your day?")
    # or 
    print("method2")
    print("Hello " + names[i] + ", how was your day?")