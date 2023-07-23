# https://judge.softuni.org/Contests/Compete/Index/1743#1

import re

pattern = r"(?<=\b_)[A-Za-z\d]+\b"
variables = re.compile(pattern)

line = input()
print(*variables.findall(line), sep=",")
