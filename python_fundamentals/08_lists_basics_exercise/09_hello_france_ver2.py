# https://judge.softuni.org/Contests/Compete/Index/1725#8

maximum_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

items_prices = [[item.split("->")[0], float(item.split("->")[1])] for item in input().split("|")]
budget = float(input())
items_sold = []

current_budget = budget
for item in items_prices:
    current_name, current_price = item
    if current_price > maximum_prices[current_name]:
        continue
    if current_price > current_budget:
        continue
    current_budget -= current_price
    items_sold.append(1.4 * current_price)

current_budget += sum(items_sold)
profit = current_budget - budget

print(" ".join(f"{pr:.2f}" for pr in items_sold))
print(f"Profit: {profit:.2f}")
print("Hello, France!") if current_budget >= 150 else print("Not enough money.")
