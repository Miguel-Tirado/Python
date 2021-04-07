# this will cause an divide by zero exception
# print(5/0)

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")
while True:
    first_num = input("\nfirst number: ")
    if first_num == 'q':
        break
    second_num = input("second number: ")
    if second_num == 'q':
        break
    
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("you cant divide by zero!")
    else:
        print(answer)
