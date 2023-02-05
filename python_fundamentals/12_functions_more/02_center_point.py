# https://judge.softuni.org/Contests/Practice/Index/1729#1
from math import sqrt, floor


def closest_to_zero(x1, y1, x2, y2):
    if sqrt(x1 ** 2 + y1 ** 2) < sqrt(x2 ** 2 + y2 ** 2):
        return floor(x1), floor(y1)
    else:
        return floor(x2), floor(y2)


a = float(input())
b = float(input())
c = float(input())
d = float(input())

result = closest_to_zero(a, b, c, d)
print(f"{result}")
