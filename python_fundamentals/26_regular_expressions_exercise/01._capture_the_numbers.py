# https://judge.softuni.org/Contests/Compete/Index/1743#0

import re

pattern = r"\d+"
regex_pattern = re.compile(pattern)

result = []
while True:
    text = input()
    if not text:
        break
    res = re.findall(regex_pattern, text)
    result.extend(res)
print(*result)
