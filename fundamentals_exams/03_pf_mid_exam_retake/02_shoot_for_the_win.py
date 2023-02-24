# https://judge.softuni.org/Contests/Practice/Index/2305#1

targets = [int(x) for x in input().split()]

shoots = 0
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if not 0 <= index < len(targets):
        continue
    target_value = targets[index]
    for i in range(len(targets)):
        if i == index:
            targets[i] = -1
            continue
        if not targets[i] == -1:
            if targets[i] > target_value:
                targets[i] -= target_value
            else:
                targets[i] += target_value
    shoots += 1

print(f"Shot targets: {shoots} -> {' '.join(str(x) for x in targets)}")
