def recognize(number):
    s = False
    ss = False
    a = "{0:b}".format(number)
    print(a)
    b = (a.replace("0", " ")).split()
    c = (a.replace("1", " ")).split()
    for i,x in enumerate(b):
        if i + 1 < len(b):
            if x == b[i+1]:
                s = True
            else:
                s = False
                break
        else:
            break
    if s:
        return True
    else:
        return False




