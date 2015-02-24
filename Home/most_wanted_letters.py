import re
def checkio(text):
    text = text.lower()
    text = re.sub('[.,;:!?]', ' ', text)
    info = {}
    for char in text:
        if char.isalpha():
            if char in info:
                info[char] += 1
            else:
                info[char] = 1
    most_wanted_letter = 0
    letter = ""
    for key in info:
        if info[key] == most_wanted_letter:
            if ord(key) < ord(letter):
                most_wanted_letter = info[key]
                letter = key
        elif info[key] > most_wanted_letter:
            most_wanted_letter = info[key]
            letter = key
    return letter

print(checkio("one"))
