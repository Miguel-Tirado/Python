print("Hello, how many people are in your dinner group today? ")
people = input()
people = int(people)

if people > 8 :
    print("\nIm sorry, but your group will have to wait for a table.")
else :
    print("\nYour table is up and ready.")