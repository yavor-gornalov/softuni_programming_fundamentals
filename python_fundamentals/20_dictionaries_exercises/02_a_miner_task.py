# https://judge.softuni.org/Contests/Practice/Index/1737#1

resources = {}

counter, key, quantity = 0, 0, 0
while True:
    command = input()
    if command == "stop":
        break
    counter += 1
    if counter % 2:
        key = command
        if key not in resources:
            resources[key] = 0
    else:
        quantity = int(command)
        resources[key] += quantity

for el in resources:
    print(f"{el} -> {resources[el]}")
