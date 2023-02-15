# https://judge.softuni.org/Contests/Practice/Index/1732#2

WALL, EMPTY, KATE = "#", " ", "k"


def get_neighbours(maze, current):
    row, col = current
    neighbours = []

    # check up
    if row > 0 and maze[row - 1][col] == EMPTY:
        neighbours.append((row - 1, col))

    # check down
    if row < len(maze) - 1 and maze[row + 1][col] == EMPTY:
        neighbours.append((row + 1, col))

    # check left
    if col > 0 and maze[row][col - 1] == EMPTY:
        neighbours.append((row, col - 1))

    # check down
    if col < len(maze[0]) - 1 and maze[row][col + 1] == EMPTY:
        neighbours.append((row, col + 1))

    return neighbours


def maze_solver(maze, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop(0)
        if current == end:
            return len(path), path
        visited.add(current)

        for neighbour in get_neighbours(maze, current):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))
    return None, None


def index_2d(maze, el):
    for row, value in enumerate(maze):
        if el in value:
            return row, value.index(el)


rows_count = int(input())
pattern = []
for _ in range(rows_count):
    r = [el for el in input()]
    pattern.append(r)
cols_count = len(pattern[0])

start_position = index_2d(maze=pattern, el=KATE)
end_positions = []
for r in range(rows_count):
    for c in range(cols_count):
        if not (r == 0 or r == rows_count - 1 or c == 0 or c == cols_count - 1):
            continue
        if pattern[r][c] in [EMPTY, KATE]:
            end_positions.append((r, c))

results = []
for end_position in end_positions:
    current_length, current_path = maze_solver(maze=pattern, start=start_position, end=end_position)
    if not current_path:
        continue
    results.append((current_length, current_path))

if results:
    print(f"Kate got out in {max(results)[0]} moves")
else:
    print("Kate cannot get out")
