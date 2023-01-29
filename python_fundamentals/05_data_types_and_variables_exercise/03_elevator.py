# https://judge.softuni.org/Contests/Compete/Index/1722#2

from math import ceil

people_count = int(input())
elevator_capacity = int(input())

courses = ceil(people_count / elevator_capacity)

print(courses)
