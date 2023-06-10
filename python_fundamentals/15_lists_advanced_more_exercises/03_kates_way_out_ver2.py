# https://judge.softuni.org/Contests/Practice/Index/3459#4

def is_outside_point(puzzle, row, col): return row < 0 or col < 0 or row >= len(puzzle) or col >= len((puzzle[0]))


def get_all_paths_length(maze, row, col, moves_counter, ways_out):
    if not 0 <= row < len(maze) or not 0 <= col < len(maze[0]):
        ways_out.append(moves_counter)
        return
    if maze[row][col] == WALL:
        return
    if maze[row][col] == KATE:
        return

    moves_counter += 1
    maze[row][col] = KATE

    get_all_paths_length(maze, row, col + 1, moves_counter, ways_out)  # RIGHT
    get_all_paths_length(maze, row + 1, col, moves_counter, ways_out)  # DOWN
    get_all_paths_length(maze, row, col - 1, moves_counter, ways_out)  # LEFT
    get_all_paths_length(maze, row - 1, col, moves_counter, ways_out)  # UP

    maze[row][col] = EMPTY

    moves_counter -= 1


WALL, EMPTY, KATE = "#", " ", "k"

size = int(input())

labyrinth = []
kate_moves = []
kate_position = [-1, -1]
for i in range(size):
    line = input()
    if KATE in line:
        kate_position = [i, line.index(KATE)]
    labyrinth.append([x for x in line])

labyrinth[kate_position[0]][kate_position[1]] = EMPTY
get_all_paths_length(labyrinth, kate_position[0], kate_position[1], 0, kate_moves)

if kate_moves:
    print(f"Kate got out in {max(kate_moves)} moves")
else:
    print("Kate cannot get out")
