# https://judge.softuni.org/Contests/Practice/Index/2525#1

import re

pattern = r"(?P<sep>[#|])(?P<name>[a-zA-Z\s]+)(?P=sep)(?P<date>\d{2}/\d{2}/\d{2})(?P=sep)(?P<calories>\d+)(?P=sep)"
regex = re.compile(pattern)

text = input()

total_calories = 0
products = []
matches = regex.finditer(text)
for match in matches:
    name = match.group("name")
    date = match.group("date")
    calories = int(match.group("calories"))

    products.append(f"Item: {name}, Best before: {date}, Nutrition: {calories}")
    total_calories += calories

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
print("\n".join(products))
