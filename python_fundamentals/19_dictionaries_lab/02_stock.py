# https://judge.softuni.org/Contests/Practice/Index/1736#1

elements = input().split()
bakery = {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}
product_search = input().split()

for product in product_search:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
