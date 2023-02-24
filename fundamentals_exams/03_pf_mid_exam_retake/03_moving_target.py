# https://judge.softuni.org/Contests/Practice/Index/2305#2

targets = [int(x) for x in input().split()]


def is_valid_index(seq, idx):
    if 0 <= idx < len(seq):
        return True
    return False


def is_radius_valid(seq, idx, rad):
    if 0 <= idx - rad < idx + rad < len(seq):
        return True
    return False


while True:
    command = input()
    if command == "End":
        break
    command_args = command.split()
    command, index = command_args[0], int(command_args[1])

    if command == "Shoot":
        power = int(command_args[2])
        if is_valid_index(seq=targets, idx=index):
            targets[index] = max(0, targets[index] - power)
            if not targets[index]:
                targets.pop(index)

    elif command == "Add":
        value = int(command_args[2])
        if is_valid_index(seq=targets, idx=index):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        radius = int(command_args[2])
        if not is_radius_valid(seq=targets, idx=index, rad=radius):
            print("Strike missed!")
            continue

        [targets.pop(index - radius) for _ in range(2 * radius + 1)]

print("|".join(str(x) for x in targets))
