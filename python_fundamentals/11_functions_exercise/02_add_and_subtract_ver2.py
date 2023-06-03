# https://judge.softuni.org/Contests/Compete/Index/1728#1

def add_and_subtract(first, second, third):
    def sum_numbers(a, b): return a + b

    def subtract(a, b): return a - b

    return subtract(sum_numbers(first, second), third)


nums = [int(input()) for _ in range(3)]
print(add_and_subtract(*nums))
