# https://judge.softuni.org/Contests/Practice/Index/1729#1

from math import sqrt, floor

points = [[float(input()) for _ in range(2)] for _ in range(2)]
closest_point_to_zero = min(points, key=lambda x: sqrt(x[0] ** 2 + x[1] ** 2))

print(tuple(floor(x) for x in closest_point_to_zero))
