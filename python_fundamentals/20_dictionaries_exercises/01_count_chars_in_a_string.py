# https://judge.softuni.org/Contests/Practice/Index/1737#0

chars = list(input())

occurrences = {}

for ch in chars:
    if ch == " ":
        continue
    if ch in occurrences:
        occurrences[ch] += 1
    else:
        occurrences[ch] = 1

for el in occurrences:
    print(f"{el} -> {occurrences[el]}")
