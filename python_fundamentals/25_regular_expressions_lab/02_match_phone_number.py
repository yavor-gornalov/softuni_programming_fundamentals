# https://judge.softuni.org/Contests/Practice/Index/1742#1
import re

phones = input()

pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
regex_pattern = re.compile(pattern)
result = re.findall(regex_pattern, phones)

print(*result, sep=", ")
