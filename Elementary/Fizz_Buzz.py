def checkio(number):
    answer = ""
    if number > 0 and number <= 1000:
        if (number % 3 == 0) and (number % 5 == 0):
            answer = "Fizz Buzz"
        elif number % 3 == 0:
            answer = "Fizz"
        elif number % 5 == 0:
            answer = "Buzz"
        else:
            answer = str(number)
        
    return answer

if __name__ == '__main__':
    print(checkio(15))
    print(checkio(6))
    print(checkio(5))
    
