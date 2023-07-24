# https://judge.softuni.org/Contests/Practice/Index/1744#1
import re

regex = {
    "name": r"%([A-Z][a-z]+)%",
    "product": r"<(\w+)>",
    "count": r"\|(\d+)\|",
    "price": r"((?:[0-9]|[1-9][0-9]+)(?:\.[0-9]+)?)\$"
}

output = []
total_income = 0
while True:
    line = input()
    if line == "end of shift":
        break

    result = []
    for key, rgx in regex.items():
        try:
            result.append(re.search(rgx, line).group(1))
        except AttributeError:
            continue

    if len(result) < 4:
        continue

    customer, product, count, price = result
    total_price = int(count) * float(price)
    total_income += total_price
    output.append(f"{customer}: {product} - {total_price:.2f}")

output.append(f"Total income: {total_income:.2f}")
[print(line) for line in output]
