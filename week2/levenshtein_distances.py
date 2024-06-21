def levenshtein(string1, string2):
    num1 = len(string1)
    num2 = len(string2)
    board = [[0] * (num1+1) for _ in range(num2+1)]

    for i in range(num2+1):
        board[i][0] = i
    for j in range(num1+1):
        board[0][j] = j

    for i in range(1, num2+1):
        for j in range(1, num1+1):
            if string2[i-1] == string1[j-1]:
                board[i][j] = board[i-1][j-1]
            else:
                board[i][j] = min(board[i-1][j], board[i]
                                  [j-1], board[i-1][j-1]) + 1

    return board[num2][num1]


print(levenshtein("yu", "you"))
