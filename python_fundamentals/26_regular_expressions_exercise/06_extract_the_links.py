# https://judge.softuni.org/Contests/Compete/Index/1743#5

import re

pattern = r"(?P<link>www\.[A-Za-z0-9]+([\-][A-Za-z0-9]+)*\.[A-Za-z]+([\.][A-Za-z]+)*)"
regex = re.compile(pattern)
links = []
while True:
    text = input()
    if not text:
        break
    matches = re.finditer(regex, text)
    for link in matches:
        links.append(link.group("link"))
[print(x) for x in links]
