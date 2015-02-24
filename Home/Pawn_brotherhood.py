def safe_pawns(pawns):
    safe = 0
    for pawn in pawns:
        left_protection = ""
        right_protection = ""
        num = 0
        for i in pawn:
            if i.isalpha():
                if ord(i) > 97 and ord(i) < 104:
                    left_pawn = chr(ord(i) - 1)
                    right_pawn = chr(ord(i) + 1)
                elif ord(i) == 97:
                    left_pawn = ""
                    right_pawn = chr(ord(i) + 1)
                elif ord(i) == 104:
                    left_pawn = chr(ord(i) - 1)
                    right_pawn = ""
            else:
                if int(i) > 1:
                    num += int(i) - 1
        left_protection += left_pawn + str(num)
        right_protection += right_pawn + str(num)    
        for item in pawns:
            if left_protection == item or right_protection == item:
                safe += 1
                break
    return safe
print(safe_pawns(["a1","a2","a3","a4","h1","h2","h3","h4"]))
