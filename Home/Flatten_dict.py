def flatten(dictionary):
    if dictionary:
        result = {}
        for item in dictionary:
            if isinstance(dictionary[item], dict):
                current_dict = flatten(dictionary[item])
                if current_dict:
                    for other in current_dict:
                        result['%s/%s' % (item, other)] = current_dict[other]
                else:
                    result[item] = ''
            else:
                result[item] = dictionary[item]
        return result
    else:
        return None

print(flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
        "place": {
               "zone": "1",
               "cell": "2"}}}))
