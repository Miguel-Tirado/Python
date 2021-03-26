# making lists for sandwhich orders and finished sandwhiches
sandwich_orders = ['pastrami','club sandwhich','pastrami','doner kebab','torta','pastrami','grilled cheese']
finished_sandwhiches = []

print("oh no we ran out of pastrami sandwhiches!")
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    current_sandwhich = sandwich_orders.pop()

    print(f"I made your {current_sandwhich.title()}.")
    finished_sandwhiches.append(current_sandwhich)

    print("\nSandwhiches made: ")
    for sandwhich in finished_sandwhiches:
        print(sandwhich.title())