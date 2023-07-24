# https://judge.softuni.org/Contests/Compete/Index/1743#5
import re

pattern = r"(?P<link>www\.[A-Za-z\d\-]+(?:\.[A-Za-z]+){1,})"
link_regex = re.compile(pattern, re.MULTILINE)

while True:
    line = input()
    if not line:
        break
    links = link_regex.findall(line)
    if links:
        [print(link) for link in links]
