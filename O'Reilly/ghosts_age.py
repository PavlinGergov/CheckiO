from fibonacci_numbers import fib_number

def checkio(opacity):
    numbs = fib_number(20)
    i = 1
    current = 10000
    while current != opacity:
        if i in numbs:
            current -= i
        else:
            current += 1
        i += 1
    return i - 1

print(checkio(9995))

