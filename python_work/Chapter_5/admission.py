age = 12
if age < 4:
    print("Your admission is free!")
elif age >= 4 and age <= 18 :
    print("your admission is $25")
else:
    print("Your admission is $40.")

# better implemention below
if age < 4:
    price = 0
elif age >= 4 and age <= 18:
    price = 25
else:
    price = 40 

print(f"\nYour admission price is ${price}.")