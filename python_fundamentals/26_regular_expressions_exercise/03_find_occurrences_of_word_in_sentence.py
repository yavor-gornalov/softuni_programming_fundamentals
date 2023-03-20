# https://judge.softuni.org/Contests/Compete/Index/1743#2

import re

text = input().lower()
word = input().lower()

result = re.findall(f"\\b{word}\\b", text)
print(len(result) if result else 0)
