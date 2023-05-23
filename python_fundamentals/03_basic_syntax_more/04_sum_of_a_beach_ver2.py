# https://judge.softuni.org/Contests/Practice/Index/1720#3

import re

input_string = input()

regex = r"sand|water|fish|sun"
keywords_count = len(re.findall(regex, input_string.lower()))

print(keywords_count)
