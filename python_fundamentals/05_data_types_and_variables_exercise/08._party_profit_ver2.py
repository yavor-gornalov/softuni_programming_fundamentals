# https://judge.softuni.org/Contests/Compete/Index/1722#7

group_size, days = [int(input()) for _ in range(2)]

coins_earned = 0
for current_day in range(1, days + 1):

    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5

    coins_earned += 50 - 2 * group_size

    if current_day % 3 == 0:
        coins_earned -= 3 * group_size
    if current_day % 5 == 0:
        coins_earned += 20 * group_size
        if current_day % 3 == 0:
            coins_earned -= 2 * group_size

print(f"{group_size} companions received {coins_earned // group_size} coins each.")
