# https://judge.softuni.org/Contests/Practice/Index/1732#4

def get_neighbours(field, position, symbol):
    row, col = position
    neighbours = []
    # check up
    if row > 0 and field[row - 1][col] == symbol:
        neighbours.append((row - 1, col))
    # check down
    if row < len(field) - 1 and field[row + 1][col] == symbol:
        neighbours.append((row + 1, col))
    # check left
    if col > 0 and field[row][col - 1] == symbol:
        neighbours.append((row, col - 1))
    # check down
    if col < len(field[0]) - 1 and field[row][col + 1] == symbol:
        neighbours.append((row, col + 1))
    return neighbours


def solver(field, position, symbol):
    stack = [position]
    visited = set()

    while stack:
        current = stack.pop()
        visited.add(current)

        for neighbour in get_neighbours(field, current, symbol):
            if neighbour not in visited:
                stack.append(neighbour)

    return visited, len(visited)


def symbol_exists(field, symbol):
    for row in range(len(field)):
        for col in range(len(field[0])):
            if symbol == field[row][col]:
                return True, (row, col)
    return False, (None, None)


# globals
DOT, DASH = ".", "-"

# get playing board from user
board = [[y for y in input().split()] for _ in range(int(input()))]

# the main loop
results = []
while True:
    dot_exists, coordinates = symbol_exists(field=board, symbol=DOT)
    if not dot_exists:
        break

    checked_points, current_result = solver(field=board, position=coordinates, symbol=DOT)

    for element in checked_points:
        r, c = element
        board[r][c] = DASH

    results.append(current_result)

print(max(results)) if results else print(0)
