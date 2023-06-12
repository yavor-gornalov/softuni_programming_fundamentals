# https://judge.softuni.org/Contests/Practice/Index/2305#0

energy = int(input())

win_counter = 0
line = input()
while line != "End of battle":
    distance = int(line)
    if distance <= energy:
        energy -= distance
        win_counter += 1
    else:
        print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        break
    if win_counter % 3 == 0:
        energy += win_counter
    line = input()
else:
    print(f"Won battles: {win_counter}. Energy left: {energy}")
