def is_prime(n):
    start = 2
    is_prime = True
    if n == 1 or n < 0:
        is_prime = False
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        start += 1   
    return is_prime

def is_int_palindrome(n):
    initial_n = n
    reverse_n = 0
    if n < 10:
        return True
    while n // 10 != 0:
        reverse_n = reverse_n*10 + n % 10
        n = n // 10
    else:
        reverse_n = reverse_n*10 + n
    if reverse_n == initial_n:
        return True
    else:
        return False

def golf(number):
    for numb in range(number + 1, 98689 + 1):
        if is_prime(numb) and is_int_palindrome(numb):
            return numb
            break
print(golf(13))