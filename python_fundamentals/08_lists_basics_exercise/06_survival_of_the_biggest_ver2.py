# https://judge.softuni.org/Contests/Compete/Index/1725#5

integers = [int(x) for x in input().split()]
n = int(input())

[integers.pop(integers.index(min(integers))) for _ in range(n)]

print(*integers, sep=", ")
