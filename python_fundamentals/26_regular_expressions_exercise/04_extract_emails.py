# https://judge.softuni.org/Contests/Compete/Index/1743#3

import re

text = input()

pattern = r"(?P<user>(([a-zA-Z0-9]+[\.\-\_]?[a-zA-Z0-9]+)))@(?P<host>(([a-z]+[-]?[a-z]+)(.[a-z]+[-]?[a-z]+)+))"
regex_pattern = re.compile(pattern)

