# https://judge.softuni.org/Contests/Practice/Index/1736#2

products = {}
while True:
    command = input()
    if command == "statistics":
        break
    command_args = command.split(": ")
    product, quantity = command_args[0], int(command_args[1])

    if product in products:
        products[product] += quantity
        continue

    products[product] = quantity

print(f"Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}\n"
      f"Total Quantity: {sum(products.values())}")
