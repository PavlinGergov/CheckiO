def checkio(data):
    
    new = []
    for item in data:
        if data.count(item) >= 2:
            new += [item]
    
    return new
