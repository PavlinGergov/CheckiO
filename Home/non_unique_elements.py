def checkio(data):
    
    new = []
    for item in data:
        if data.count(item) >= 2:
            new += [item]
    
    return new

if __name__ == "__main__":
    print(checkio([1, 2, 3, 1, 3]))
    print(checkio([1, 2, 3, 4, 5])) 
    print(checkio([5, 5, 5, 5, 5]))
    print(checkio([10, 9, 10, 10, 9, 8]))
