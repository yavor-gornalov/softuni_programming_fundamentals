# https://judge.softuni.org/Contests/Compete/Index/1719#10

budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = (1 + 0.25) * flour_price

bread_price = 1 * flour_price + 1 * eggs_price + 0.25 * milk_price
loaves_of_bread = 0
colored_eggs_count = 0

while True:
    if bread_price > budget:
        break
    budget -= bread_price
    loaves_of_bread += 1
    colored_eggs_count += 3

    if loaves_of_bread % 3 == 0:
        colored_eggs_count -= loaves_of_bread - 2

print(f"You made {loaves_of_bread} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
