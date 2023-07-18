# https://judge.softuni.org/Contests/Compete/Index/1737#5

products = {}

line = input()
while line != "buy":
    product, *args = line.split()
    price, quantity = [float(x) for x in args]

    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["price"] = price
        products[product]["quantity"] += quantity

    line = input()

for product, data in products.items():
    print(f"{product} -> {data['price'] * data['quantity']:.2f}")
