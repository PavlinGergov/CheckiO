def house_password(data):
    
    is_lowercase = False
    is_uppercase = False
    is_number = False
    
    for char in data:
        if char.islower():
            is_lowercase = True
        elif char.isupper():
            is_uppercase = True
        elif int(char) in range(0, 10):
            is_number = True

    if len(data) >= 10:
        if is_lowercase and is_uppercase and is_number:
            return True
        else:
            return False
    else:
        return False

print(house_password('QwErTy911poqqqq'))
print(house_password('123456123456'))
    

