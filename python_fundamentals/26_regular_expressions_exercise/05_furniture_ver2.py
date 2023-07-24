# https://judge.softuni.org/Contests/Compete/Index/1743#4
import re

pattern = r"^\>\>(?P<product>\w+)\<\<(?P<price>[1-9][\.0-9]*)\!(?P<count>\d+)\b"
info = re.compile(pattern)

total_cost = 0
products = []
while True:
    line = input()
    if line == "Purchase":
        break
    result = info.findall(line)
    if result:
        for product, price, count in result:
            total_cost += float(price) * int(count)
            products.append(product)

print(f"Bought furniture:")
[print(product) for product in products]
print(f"Total money spend: {total_cost:.2f}")
