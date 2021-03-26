# simple while loop that acts like a for loop
# it will iterate 5 times

number = 1

while number <= 5:
    print(number)
    number += 1

# adding a while loop that uses the continue
print("\n------------while loop with continue--------------")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0 :
        continue
    print(current_number)