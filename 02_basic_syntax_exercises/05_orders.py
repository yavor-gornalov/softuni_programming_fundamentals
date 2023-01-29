# https://judge.softuni.org/Contests/Compete/Index/1719#4

def order(price, period, per_day):
    return period * per_day * price


def is_data_valid(price, period, per_day):
    is_valid = False
    if 0.01 <= price <= 100 and \
            1 <= period <= 31 and \
            1 <= per_day <= 2000:
        is_valid = True
    return is_valid


# main
n = int(input())

total_price = 0
for _ in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if is_data_valid(price_per_capsule, days, capsules_per_day):
        order_price = order(price_per_capsule, days, capsules_per_day)
        print(f"The price for the coffee is: ${order_price:.2f}")
        total_price += order_price
else:
    print(f"Total: ${total_price:.2f}")
