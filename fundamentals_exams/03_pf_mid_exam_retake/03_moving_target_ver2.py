# https://judge.softuni.org/Contests/Practice/Index/2305#2

def shoot_target(index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        targets.pop(index) if targets[index] <= 0 else None
        return 1
    return 0


def add_target(index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
        return 1
    print("Invalid placement!")
    return 0


def strike_targets(index, radius):
    if radius <= index < len(targets) - radius:
        [targets.pop(index - radius) for _ in range(2 * radius + 1)]
        return 1
    print("Strike missed!")
    return 0


commands = {
    "Shoot": shoot_target,
    "Add": add_target,
    "Strike": strike_targets
}

targets = [int(x) for x in input().split()]

while True:
    line = input()
    if line == "End":
        print(*targets, sep="|")
        break

    action, *tokens = line.split()
    commands[action](int(tokens[0]), int(tokens[1]))
