# https://judge.softuni.org/Contests/Compete/Index/1743#1

import re

text = input()

pattern = r"(?<=\b_)[A-Za-z0-9]+\b"
regex_pattern = re.compile(pattern)
result = re.findall(regex_pattern, text)

print(*result, sep=",")
