# https://judge.softuni.org/Contests/Practice/Index/1732#3

from collections import deque

size = int(input())

battle_ships_coordinates = {}
for i in range(size):
    row = [int(x) for x in input().split()]
    for j, value in enumerate(row):
        if value > 0:
            battle_ships_coordinates[f"{i}-{j}"] = value

attacked_ships = deque(input().split())
while battle_ships_coordinates and attacked_ships:
    ship = attacked_ships.popleft()
    if ship in battle_ships_coordinates:
        battle_ships_coordinates[ship] -= 1

print(len([x for x in battle_ships_coordinates.values() if x <= 0]))
