# https://judge.softuni.org/Contests/Practice/Index/2303#1

import re

pattern = r"^\@\#+(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])\@\#+$"
barcode_regex = re.compile(pattern)

for _ in range(int(input())):
    matches = barcode_regex.match(input())
    if matches:
        barcode = matches.group("barcode")
        nums_pattern = r"\d"
        result = re.findall(nums_pattern, barcode)
        group = "".join(result) if result else "00"
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")
