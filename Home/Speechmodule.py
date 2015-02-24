FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    is_first = False
    is_second = False
    word = ""
    if number // 100 != 0:
        first = number // 100
        word += FIRST_TEN[first - 1] + " hundred"
        is_first = True
    if (number // 10) % 10 != 0 :
        if is_first:
            word += " "
        second = (number // 10) % 10
        if second == 1:
            word += SECOND_TEN[number % 10]
        else:
            word += OTHER_TENS[second - 2]
            is_second = True
    else:
        if is_first:
            is_second = True
    if number % 10 != 0:
        if is_second:
            word += " "
            word += FIRST_TEN[number % 10 - 1]
    if number // 10 == 0:
        word += FIRST_TEN[number % 10 - 1]
            
    return word
            
print(checkio(302))
