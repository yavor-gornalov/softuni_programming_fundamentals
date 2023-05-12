# https://judge.softuni.org/Contests/Compete/Index/1719#4

number_of_orders = int(input())

total_price = 0
for _ in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= capsule_price <= 100:
        continue

    if not 1 <= days <= 31:
        continue

    if not 1 <= capsules_per_day <= 2000:
        continue

    price = days * capsules_per_day * capsule_price
    print(f"The price for the coffee is: ${price:.2f}")

    total_price += price


print(f"Total: ${total_price:.2f}")
