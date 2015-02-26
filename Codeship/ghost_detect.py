def recognize(number):
    is_true = False
    binary_number = "{0:b}".format(number)
    ones = (binary_number.replace("0", " ")).split()
    for index,numb in enumerate(ones):
        if index + 1 < len(ones):
            if numb == ones[index+1]:
                is_true = True
            else:
                is_true = False
                break
        else:
            break
    if is_true:
        return True
    else:
        return False

print(recognize(21))
print(recognize(3687))





