# https://judge.softuni.org/Contests/Practice/Index/1742#0

import re

names = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
regex_pattern = re.compile(pattern)
result = re.findall(regex_pattern, names)

print(*result)
