# https://judge.softuni.org/Contests/Practice/Index/1737#5

products_by_price = {}
products_by_quantity = {}
while True:
    command = input()
    if command == "buy":
        break
    command_args = command.split()
    name, price, quantity = command_args[0], float(command_args[1]), int(command_args[2])
    products_by_price[name] = price
    if name not in products_by_quantity:
        products_by_quantity[name] = quantity
    else:
        products_by_quantity[name] += quantity

for name in products_by_price:
    print(f"{name} -> {products_by_price[name] * products_by_quantity[name]:.2f}")
