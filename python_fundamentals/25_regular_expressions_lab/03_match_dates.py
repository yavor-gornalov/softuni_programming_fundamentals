# https://judge.softuni.org/Contests/Practice/Index/1742#2

import re

text = input()

pattern = r"\b(?P<Day>(\d{2}))(?P<sep>([\./-]))(?P<Month>([A-Z][a-z]{2}))(?P=sep)(?P<Year>(\d{4}))\b"
regex_pattern = re.compile(pattern)
dates = re.finditer(regex_pattern, text)

for date in dates:
    date_data = date.groupdict()
    print(f"Day: {date_data['Day']}, Month: {date_data['Month']}, Year: {date_data['Year']}")
