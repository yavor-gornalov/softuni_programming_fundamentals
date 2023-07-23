# https://judge.softuni.org/Contests/Compete/Index/1743#2

import re

text = input()
target = input()

pattern = rf"\b{target}\b"
regex = re.compile(pattern, re.IGNORECASE)
print(len(regex.findall(text)))
