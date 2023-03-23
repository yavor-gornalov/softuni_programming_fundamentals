# https://judge.softuni.org/Contests/Practice/Index/1744#1
import re

patterns = {
    "name": r"^\%(?P<name>[A-Z][a-z]+)\%",
    "product": r"\<(?P<product>\w+)\>",
    "count": r"\|(?P<count>\d+)\|",
    "price": r"(?P<price>([0-9]|[1-9][0-9]+)(\.[0-9]+)?)\$$"
}

redex_patterns = {k: re.compile(val) for k, val in patterns.items()}

total_price = 0
while True:
    line = input()
    if line == "end of shift":
        break
    try:
        name = re.search(redex_patterns["name"], line).group("name")
        product = re.search(redex_patterns["product"], line).group("product")
        count = re.search(redex_patterns["count"], line).group("count")
        price = re.search(redex_patterns["price"], line).group("price")
    except AttributeError:
        continue
    current_price = int(count) * float(price)
    total_price += current_price
    print(f"{name}: {product} - {current_price:.2f}")
print(f"Total income: {total_price:.2f}")
