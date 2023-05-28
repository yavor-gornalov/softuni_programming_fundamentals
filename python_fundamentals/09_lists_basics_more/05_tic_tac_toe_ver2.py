# https://judge.softuni.org/Contests/Practice/Index/1726#4


def row_winner():
    for player in players:
        for row in range(size):
            if all(x == player for x in playground[row]):
                return player
    return 0


def column_winner():
    for player in players:
        for col in range(size):
            column = []
            for row in range(size):
                column.append(playground[row][col])

            if all(x == player for x in column):
                return player
    return 0


def diagonal_winner():
    left_diagonal, right_diagonal = [], []

    for i in range(size):
        left_diagonal.append(playground[i][i])
        right_diagonal.append(playground[i][size - i - 1])

    for player in players:
        if all(x == player for x in left_diagonal) or all(x == player for x in right_diagonal):
            return player
    return 0


def gameplay():
    winner = row_winner()
    if winner:
        return winner

    winner = column_winner()
    if winner:
        return winner

    winner = diagonal_winner()
    if winner:
        return winner


players = [1, 2]
size = 3
playground = [[int(x) for x in input().split()] for _ in range(size)]

game_winner = gameplay()

if game_winner == players[0]:
    print("First player won")
elif game_winner == players[1]:
    print("Second player won")
else:
    print("Draw!")
