def check_connection(network, first, second):
    all_friends = []
    for items in network:
        items = items.split('-')
        all_friends.append(items)
        
    first_friends = [first]
    is_true = True
    
    while is_true:
        seen = 0
        for index, item in enumerate(all_friends):
            print(item)
            if item[0] in first_friends:
                first_friends.append(item[1])
                seen += 1
                del all_friends[index]
            elif item[1] in first_friends:
                first_friends.append(item[0])
                seen += 1
                del all_friends[index]
            
        if seen == 0 or len(all_friends) == 0:
            is_true = False
    
    if second in first_friends:
        return True
    else:
        return False


