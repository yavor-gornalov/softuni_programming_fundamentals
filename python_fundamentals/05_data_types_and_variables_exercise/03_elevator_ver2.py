# https://judge.softuni.org/Contests/Compete/Index/1722#2
from math import ceil

nuber_of_people, capacity = [int(input()) for _ in range(2)]

print(ceil(nuber_of_people / capacity))
