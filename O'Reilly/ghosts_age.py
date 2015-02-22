def fib_number(n):
    fib = [1, 1]
    s = 0
    i = 1
    if n == 2:
        return 2
    elif n > 2:
        while i < n:
            s = fib[i-1] + fib[i]
            fib.append(s)
            i += 1

    return fib

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

print(checkio(4000))
            

