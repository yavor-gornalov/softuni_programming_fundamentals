# https://judge.softuni.org/Contests/Practice/Index/1726#4

matrix = list()
n = 3

for _ in range(3):
    matrix.append([x for x in input().split()])

has_winner = False
player_1_wins, player_2_wins = False, False
# checking rows
for row in matrix:
    player_1_wins = all(element == "1" for element in row)
    player_2_wins = all(element == "2" for element in row)

    if player_1_wins or player_2_wins:
        has_winner = True
        break

# checking columns
if not has_winner:
    for col in range(n):
        column = []
        for row in range(n):
            column.append(matrix[row][col])

        player_1_wins = all(element == "1" for element in column)
        player_2_wins = all(element == "2" for element in column)

        if player_1_wins or player_2_wins:
            has_winner = True
            break

# checkin diagonals
if not has_winner:
    diagonal_1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    diagonal_2 = [matrix[0][2], matrix[1][1], matrix[2][0]]

    player_1_wins = all(element == "1" for element in diagonal_1) or all(element == "1" for element in diagonal_2)

    player_2_wins = all(element == "2" for element in diagonal_1) or all(element == "2" for element in diagonal_2)

    if player_1_wins or player_2_wins:
        has_winner = True

if player_1_wins:
    print("First player won")
elif player_2_wins:
    print("Second player won")
else:
    print("Draw!")
