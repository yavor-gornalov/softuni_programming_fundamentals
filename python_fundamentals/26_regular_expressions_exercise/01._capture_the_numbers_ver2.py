# https://judge.softuni.org/Contests/Compete/Index/1743#0

import re

pattern = r"\d+"
numbers = re.compile(pattern)

result = []
while True:
    line = input()
    if not line:
        break
    result += (numbers.findall(line))

print(*result, sep=" ")
