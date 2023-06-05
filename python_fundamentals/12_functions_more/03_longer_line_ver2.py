# https://judge.softuni.org/Contests/Practice/Index/1729#2

from math import sqrt, floor


def distance_to_central_point(point):
    return sqrt(point[0] ** 2 + point[1] ** 2)


def line_length(line):
    return sqrt((line[1][0] - line[0][0]) ** 2 + (line[1][1] - line[0][1]) ** 2)


def swap_line(line):
    if distance_to_central_point(line[0]) > distance_to_central_point(line[1]):
        line[0], line[1] = line[1], line[0]


first_line = [[float(input()) for _ in range(2)] for _ in range(2)]
second_line = [[float(input()) for _ in range(2)] for _ in range(2)]

longer_line = max(first_line, second_line, key=line_length)
swap_line(longer_line)

print(tuple(floor(x) for x in longer_line[0]), tuple(floor(x) for x in longer_line[1]), sep="")
