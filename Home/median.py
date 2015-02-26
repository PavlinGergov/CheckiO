def find_median(data):
    
    data_sorted = sorted(data)
    
    if len(data_sorted) % 2 == 0:
        right_median = data_sorted[int(len(data) / 2)]
        left_median = data_sorted[int((len(data)) / 2) - 1]
        median = (right_median + left_median) / 2
        return median
    else:
        median = data_sorted[(len(data_sorted) // 2)]
        return median

