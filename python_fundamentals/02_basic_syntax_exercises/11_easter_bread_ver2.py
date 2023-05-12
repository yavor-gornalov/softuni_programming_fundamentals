# https://judge.softuni.org/Contests/Compete/Index/1719#10

budget = float(input())
flour_price = float(input())

pack_of_eggs_price = 0.75 * flour_price
quarter_of_milk = (1.25 * flour_price) / 4
loaf_price = flour_price + pack_of_eggs_price + quarter_of_milk

total_eggs, total_bread = 0, 0
while True:
    if budget - loaf_price < 0:
        break

    budget -= loaf_price
    total_eggs += 3
    total_bread += 1

    if total_bread % 3 == 0:
        total_eggs -= (total_bread - 2)

print(f"You made {total_bread} loaves of Easter bread! Now you have {total_eggs} eggs and {budget:.2f}BGN left.")
