# https://judge.softuni.org/Contests/Practice/Index/1732#4

def is_position_inside(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def find_area(matrix, row, col):
    if not is_position_inside(matrix, row, col):
        return 0
    if matrix[row][col] != EMPTY:
        return 0

    result = 1
    matrix[row][col] = VISITED

    result += find_area(matrix, row, col + 1)  # RIGHT
    result += find_area(matrix, row, col - 1)  # LEFT
    result += find_area(matrix, row + 1, col)  # DOWN
    result += find_area(matrix, row - 1, col)  # UP

    return result


EMPTY, WALL, VISITED = ".", "-", "v"
n = int(input())
board = [input().split() for _ in range(n)]

max_size_area = 0
for r in range(n):
    for c in range(len(board[0])):
        max_size_area = max(
            max_size_area,
            find_area(board, r, c)
        )

print(max_size_area)
