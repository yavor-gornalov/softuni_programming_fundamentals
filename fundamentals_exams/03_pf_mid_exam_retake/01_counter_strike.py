# https://judge.softuni.org/Contests/Practice/Index/2305#0

energy = int(input())

battles_won, is_alive = 0, True
command = input()
while not command == "End of battle":
    distance = int(command)
    if energy < distance:
        is_alive = False
        break
    battles_won += 1
    energy -= distance
    if not battles_won % 3:
        energy += battles_won
    command = input()

if is_alive:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
