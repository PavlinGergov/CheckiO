def checkio(data):
    is_lowercase = False
    is_uppercase = False
    is_number = False
    is_length = False
    is_strong = False
    
    for char in data:
        if char.islower():
            is_lowercase = True
        elif char.isupper():
            is_uppercase = True
        elif int(char) in range(0, 10):
            is_number = True

    if len(data) >= 10:
        is_length = True
    
    if is_lowercase and is_uppercase and is_number and is_length:
        is_strong = True
    
    return is_strong

if __name__ == '__main__':
    print(checkio('bAse730onE4'))
    print(checkio('A1213pokl'))
