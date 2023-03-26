# https://judge.softuni.org/Contests/Practice/Index/2518#1

import re

pattern = r"(\=|/)([A-Z][a-zA-Z]{2,})(\1)"
regex = re.compile(pattern)

text = input()
results = regex.findall(text)

locations = []
for result in results:
    locations.append(result[1])

travel_points = sum([len(location) for location in locations])
print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {travel_points}")
