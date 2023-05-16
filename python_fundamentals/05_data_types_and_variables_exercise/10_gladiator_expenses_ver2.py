# https://judge.softuni.org/Contests/Compete/Index/1722#9

equipment_prices = dict.fromkeys(("helmet", "sword", "shield", "armor"), 0.0)

fights_count = int(input())

for key in equipment_prices:
    equipment_prices[key] = float(input())

total_cost = 0
for fight in range(1, fights_count + 1):
    if fight % 2 == 0:
        total_cost += equipment_prices["helmet"]
    if fight % 3 == 0:
        total_cost += equipment_prices["sword"]
    if fight % 6 == 0:
        total_cost += equipment_prices["shield"]
    if fight % 12 == 0:
        total_cost += equipment_prices["armor"]

print(f"Gladiator expenses: {total_cost:.2f} aureus")
