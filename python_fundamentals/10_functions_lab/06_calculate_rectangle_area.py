# https://judge.softuni.org/Contests/Practice/Index/1727#5
from decimal import Decimal


# rectangle_area = lambda a, b: Decimal(a * b)
def rectangle_area(a, b): return Decimal(a * b)


side_a = float(input())
side_b = float(input())
print(rectangle_area(a=side_a, b=side_b))
