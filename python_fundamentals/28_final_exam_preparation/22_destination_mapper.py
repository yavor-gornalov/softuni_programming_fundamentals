# https://judge.softuni.org/Contests/Practice/Index/2518#1
import re

line = input()
pattern = r"(\=|\/)(?P<dst>[A-Z][A-Za-z]{2,})\1"
result = re.finditer(pattern, line)

travel_points = 0
destinations = []
for match in result:
    current_place = match.group("dst")
    destinations.append(current_place)
    travel_points += len(current_place)

print(f"Destinations: {', '.join(d for d in destinations)}\n"
      f"Travel Points: {travel_points}")
