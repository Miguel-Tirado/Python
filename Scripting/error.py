def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:   # note we can remove the ZeroDivisionError to catch all types of errors
        print('Error: you tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))   
print(div42by(1))