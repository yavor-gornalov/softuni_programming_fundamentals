# https://judge.softuni.org/Contests/Practice/Index/1729#2

from math import sqrt, floor


def normalize_line(line):
    if sqrt(line[0] ** 2 + line[1] ** 2) > sqrt(line[2] ** 2 + line[3] ** 2):
        line = line[2:4] + line[0:2]
    return line


def line_length(line): return sqrt((line[2] - line[0]) ** 2 + (line[3] - line[1]) ** 2)


def longer_line(line_1, line_2):
    if line_length(line_1) >= line_length(line_2):
        return line_1
    return line_2


first_line, second_line = [], []
for _ in range(4):
    first_line.append(float(input()))
for _ in range(4):
    second_line.append(float(input()))

result = normalize_line(longer_line(first_line, second_line))

for i, value in enumerate(result):
    result[i] = floor(value)

print(f"({result[0]}, {result[1]})({result[2]}, {result[3]})")
