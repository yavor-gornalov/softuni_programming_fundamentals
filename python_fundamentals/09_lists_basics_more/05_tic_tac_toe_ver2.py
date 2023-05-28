# https://judge.softuni.org/Contests/Practice/Index/1726#4


def row_winner(symbol):
    for row in range(size):
        if all(x == symbol for x in playground[row]):
            return 1
    return 0


def column_winner(symbol):
    for col in range(size):
        column = []
        for row in range(size):
            column.append(playground[row][col])
        if all(x == symbol for x in column):
            return 1
    return 0


def diagonal_winner(symbol):
    left_diagonal, right_diagonal = [], []
    for i in range(size):
        left_diagonal.append(playground[i][i])
        right_diagonal.append(playground[i][size - i - 1])

    if all(x == symbol for x in left_diagonal) or all(x == symbol for x in right_diagonal):
        return 1
    return 0


def gameplay():
    for player in players:
        if row_winner(player) or column_winner(player) or diagonal_winner(player):
            return player
    return 0


players = ["1", "2"]
size = 3
playground = [input().split() for _ in range(size)]

winner = gameplay()

if winner == players[0]:
    print("First player won")
elif winner == players[1]:
    print("Second player won")
else:
    print("Draw!")
