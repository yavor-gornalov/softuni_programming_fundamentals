# https://judge.softuni.org/Contests/Practice/Index/2517#0

def print_receipt(neto, tax, price):
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {neto:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {price:.2f}$")


neto_price, tax_price, total_price = 0, 0, 0
TAX_MULTIPLIER, DISCOUNT = 0.20, 0.10
while True:
    command = input()
    if command == "regular":
        break
    elif command == "special":
        total_price -= DISCOUNT * total_price
        break
    current_price = float(command)
    if not current_price > 0:
        print("Invalid price!")
        continue
    neto_price += current_price
    tax_price += TAX_MULTIPLIER * current_price
    total_price = neto_price + tax_price

if not total_price:
    print("Invalid order!")
else:
    print_receipt(neto=neto_price, tax=tax_price, price=total_price)
