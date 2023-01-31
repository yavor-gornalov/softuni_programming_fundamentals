# https://judge.softuni.org/Contests/Compete/Index/1725#8

items = input().split("|")
budget = float(input())

bought_items, sold_items = [], []
for item in items:
    item_type, item_price = item.split('->')
    item_price = float(item_price)

    if item_type == "Clothes" and 0 <= item_price <= 50.00 or \
            item_type == "Shoes" and 0 <= item_price <= 35.00 or \
            item_type == "Accessories" and 0 <= item_price <= 20.50:

        if item_price <= budget:
            budget -= item_price
            bought_items.append(item_price)

sum_of_bought_items = sum(bought_items)

for prise in bought_items:
    sold_items.append((1 + 0.40) * prise)

sum_of_sold_items = sum(sold_items)
profit = sum_of_sold_items - sum_of_bought_items
budget += sum_of_sold_items

for i in range(len(sold_items)):
    print(f"{sold_items[i]:.2f}", end=' ')
print(f"\nProfit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
