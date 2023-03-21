# https://judge.softuni.org/Contests/Compete/Index/1743#4

import re

pattern = r"\>\>(?P<product>[a-zA-Z]+)\<\<(?P<price>([0-9]|[1-9][0-9]+)(\.[0-9]+)*)\!(?P<count>\d+)"
regex_pattern = re.compile(pattern)

products = []
total_cost = 0
while True:
    purchase = input()
    if purchase == "Purchase":
        break
    matches = re.finditer(regex_pattern, purchase)
    for match in matches:
        furniture_data = match.groupdict()
        products.append(furniture_data["product"])
        price = float(furniture_data["price"])
        count = int(furniture_data["count"])
        total_cost += price * count

print(f"Bought furniture:")
[print(product) for product in products]
print(f"Total money spend: {total_cost:.2f}")
