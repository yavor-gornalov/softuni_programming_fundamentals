# https://judge.softuni.org/Contests/Practice/Index/1730#4

names = list(map(str, input().split(", ")))

names_sorted = sorted(names, reverse=False, key=lambda name: (-len(name), name))
print(names_sorted)
