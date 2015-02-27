def feed_pigeons(n):
    all_pigeons = []
    counter = 0
    pigeons = 1
    while n > 0:
        i = 0
        while i < pigeons: 
            all_pigeons.append(0)
            i += 1
        for index, bird in enumerate(all_pigeons):
            if n > 0:
                all_pigeons[index] += 1
                n -= 1
            else:
                break
        pigeons += 1
    for pign in all_pigeons:
        if pign != 0:
            counter += 1

    return counter

print(feed_pigeons(5))
