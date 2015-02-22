import re

VOWELS = "AEIOUY"
vowels = "aeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
consonants = "bcdfghjklmnpqrstvwxz"

def checkio(text):
    counter = 0
    is_alternating = False
    text = re.sub('[.,;:!?]', ' ', text)
    text = text.split()
    print(text)
    for item in text: 
        if item.isalpha():
            i = 0
            while i < len(item):
                if len(item) == 1:
                    break
                
                if (item[i] in vowels or item[i] in VOWELS) and (i+1 < len(item)):
                    if item[i+1] in consonants or item[i+1] in CONSONANTS:
                        is_alternating = True
                    else:
                        is_alternating = False
                        break
                elif (item[i] in consonants or item[i] in CONSONANTS) and (i+1 < len(item)):
                    if item[i+1] in vowels or item[i+1] in VOWELS:
                        is_alternating = True
                    else:
                        is_alternating = False
                        break
                else:
                    if is_alternating:
                        counter += 1
                    break
                            
                i += 1

    return counter