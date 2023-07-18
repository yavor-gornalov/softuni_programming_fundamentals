# https://judge.softuni.org/Contests/Compete/Index/1737#1

resources = {}

while True:
    key = input()
    if key == "stop":
        break
    value = int(input())

    if key not in resources:
        resources[key] = 0
    resources[key] += value

for key, value in resources.items():
    print(f"{key} -> {value}")
