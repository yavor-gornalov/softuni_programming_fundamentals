# https://judge.softuni.org/Contests/Compete/Index/1719#11

quantity = int(input())
days = int(input())

ornament_price = 2
skirt_price = 5
garland_price = 3
lights_price = 15

ornament_spirit = 5
skirt_spirit = 3
garland_spirit = 10
lights_spirit = 17

total_cost = 0
total_spirit = 0
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += quantity * ornament_price
        total_spirit += ornament_spirit
    if day % 3 == 0:
        total_cost += quantity * (skirt_price + garland_price)
        total_spirit += skirt_spirit + garland_spirit
    if day % 5 == 0:
        total_cost += quantity * lights_price
        total_spirit += lights_spirit
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_cost += skirt_price + garland_price + lights_price
        total_spirit -= 20
        if day == days:
            total_spirit -= 30

print(f"Total cost: {total_cost}\n"
      f"Total spirit: {total_spirit}")
