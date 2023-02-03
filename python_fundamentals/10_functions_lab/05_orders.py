# https://judge.softuni.org/Contests/Practice/Index/1727#4

COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACK = 2.00


def total_price(product: str, quantity: int):
    price = None
    if product == "coffee":
        price = COFFEE
    elif product == "coke":
        price = COKE
    elif product == "water":
        price = WATER
    elif product == "snacks":
        price = SNACK
    return price * quantity


product_input = input()
quantity_input = int(input())
result = total_price(product=product_input, quantity=quantity_input)
print(f"{result:.2f}")
