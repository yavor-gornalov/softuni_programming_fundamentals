# https://judge.softuni.org/Contests/Compete/Index/1722#7

companions_count = int(input())
days = int(input())

money_earned = 0
money_per_day = 50
costs_for_food = 2
costs_for_water = 3
additional_costs = 2
earns_for_monster_killed = 20

for day in range(1, days + 1):
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5

    money_earned += money_per_day - companions_count * costs_for_food

    if day % 3 == 0:
        money_earned -= companions_count * costs_for_water
    if day % 5 == 0:
        money_earned += companions_count * earns_for_monster_killed
        if day % 3 == 0:
            money_earned -= companions_count * additional_costs

companion_earn = money_earned // companions_count

print(f"{companions_count} companions received {companion_earn} coins each.")
