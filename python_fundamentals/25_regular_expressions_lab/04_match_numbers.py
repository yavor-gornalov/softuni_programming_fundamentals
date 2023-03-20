# https://judge.softuni.org/Contests/Practice/Index/1742#3

import re

text = input()

pattern = r"(^|(?<=\s))(\-?)([0-9]|[1-9][0-9]+)(\.[0-9]+)?($|(?=\s))"
regex_pattern = re.compile(pattern)
numbers = re.finditer(regex_pattern, text)

for number in numbers:
    print(number.group(), end=" ")
