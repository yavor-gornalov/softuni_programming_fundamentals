# https://judge.softuni.org/Contests/Compete/Index/1737#0

text = input()

occurrences = {}
for ch in text:
    if ch == " ":
        continue
    if ch not in occurrences:
        occurrences[ch] = 0
    occurrences[ch] += 1

for ch, occ in occurrences.items():
    print(f"{ch} -> {occ}")
