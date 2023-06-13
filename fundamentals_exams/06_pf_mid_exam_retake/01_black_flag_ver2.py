# https://judge.softuni.org/Contests/Practice/Index/1773#0

days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0
current_day = 1
while current_day <= days:
    current_plunder = daily_plunder
    if current_day % 3 == 0:
        current_plunder *= 1.5

    total_plunder += current_plunder

    if current_day % 5 == 0:
        total_plunder -= 0.3 * total_plunder

    current_day += 1

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {100 * (total_plunder / expected_plunder):.2f}% of the plunder.")
