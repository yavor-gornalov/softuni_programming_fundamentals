# https://judge.softuni.org/Contests/Practice/Index/1732#3

def attack(field, coordinates):
    row, col = coordinates
    ship_destroyed = False
    if 0 < field[row][col] <= 1:
        field[row][col] = 0
        ship_destroyed = True
    field[row][col] -= 1
    return ship_destroyed


# get battlefield
battlefield = [[int(r) for r in input().split()] for _ in range(int(input()))]
# get attacked squares
attack_sequence = [[int(coordinates) for coordinates in square.split("-")] for square in input().split()]

# battle started
destroy_counter = 0
for attacked_square in attack_sequence:
    destroy_counter += attack(field=battlefield, coordinates=attacked_square)

print(destroy_counter)
