# https://judge.softuni.org/Contests/Compete/Index/1740#8
import re

text = input()
regex = re.compile(r"(\D+)(\d+)")

match = regex.findall(text)

symbols_used = set()
output_text = ""
for substring, number_str in match:
    [symbols_used.add(s.upper()) for s in substring]
    output_text += substring.upper() * int(number_str)

print(f"Unique symbols used: {len(symbols_used)}\n{output_text}")
