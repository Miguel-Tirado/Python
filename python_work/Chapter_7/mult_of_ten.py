# This program tells the user if the number
# they enter is a multiple of ten 

print("Enter a number and I'll tell you if its a multiple of ten or not")
num = input()
num = int(num)

if num % 10 == 0: 
    print(f"The number {num} is a multiple of 10.")
else:
    print(f"The number {num} is not a multiple of 10.")