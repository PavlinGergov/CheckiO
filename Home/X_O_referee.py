def checkio(game_result):
    winner = "D"
    for item in game_result:
        if item[0] == item[1] and item[1] == item[2]:
            if item[0].isalpha():
                winner = item[0]
                break
    i = 0
    while i < 3:
        if game_result[0][i] == game_result[1][i] and game_result[1][i] == game_result[2][i]:
            if game_result[0][i].isalpha():
                winner = game_result[0][i]
                break
        i += 1
    if (game_result[0][0] == game_result[1][1] and game_result[1][1] == game_result[2][2]) or (game_result[0][2] == game_result[1][1] and game_result[1][1] == game_result[2][0]):
        if game_result[1][1].isalpha():
            winner = game_result[1][1]
    return winner

print(checkio(["OO.", "XOX", "XOX"]))
