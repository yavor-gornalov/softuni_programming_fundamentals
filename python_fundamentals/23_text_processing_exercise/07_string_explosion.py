# https://judge.softuni.org/Contests/Compete/Index/1740#6

text = list(input())

power, result = 0, ""
for i in range(1, len(text) + 1):
    prev = text[i - 1]
    if prev == ">":
        power += int(text[i])
        result += prev
    else:
        if not power:
            result += prev
        power = max(0, power - 1)

print(result)
