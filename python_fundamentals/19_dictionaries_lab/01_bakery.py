# https://judge.softuni.org/Contests/Practice/Index/1736#0

elements = input().split()

bakery = {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}

print(bakery)
