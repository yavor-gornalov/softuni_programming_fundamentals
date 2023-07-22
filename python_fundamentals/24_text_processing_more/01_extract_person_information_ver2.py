# https://judge.softuni.org/Contests/Practice/Index/1741#0

import re

persons_count = int(input())
name_pattern = r"@([A-Za-z]+)\|"
age_pattern = r"\#(\d+)\*"

for _ in range(persons_count):
    info = input()
    name = re.findall(name_pattern, info)
    age = re.findall(age_pattern, info)
    if name and age:
        print(f"{name[0]} is {age[0]} years old.")
