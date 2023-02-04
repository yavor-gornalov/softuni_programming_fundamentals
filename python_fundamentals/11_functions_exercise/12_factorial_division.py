# https://judge.softuni.org/Contests/Compete/Index/1728#11

def factorial_diff(m, n):
    # n! = n * (n - 1)!
    start = min(m, n) + 1
    end = max(m, n) + 1
    fact = 1
    for i in range(start, end):
        fact *= i
    return fact


a = int(input())
b = int(input())

print(f"{factorial_diff(a, b):.2f}")
