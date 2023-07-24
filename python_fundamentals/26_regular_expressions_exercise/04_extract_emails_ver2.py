# https://judge.softuni.org/Contests/Compete/Index/1743#3

import re

text = input()
pattern = r"(?<!\S)([A-Za-z\d]+[\.\-\_]*[A-Za-z\d]+@[A-Za-z]+[\-]*[A-Za-z]+\.[A-Za-z]+[\-\.]*[A-Za-z]+)\b"

result = re.findall(pattern, text)
for email in result:
    print(email)
