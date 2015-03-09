def count_gold(pyramid):
    work = list(list(row) for row in pyramid)
    for i in range(len(work) - 1, -1 , -1):
        if i < len(work) - 1:
            for j in range(len(work[i])):
                work[i][j] += max(work[i+1][j], work[i+1][j+1])
    return work[0][0]

pyramid = ((1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3))
print(count_gold(pyramid))