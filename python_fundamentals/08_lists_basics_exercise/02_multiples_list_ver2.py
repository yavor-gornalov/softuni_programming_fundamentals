# https://judge.softuni.org/Contests/Compete/Index/1725#1

factor, count = [int(input()) for _ in range(2)]

result = [factor * i for i in range(1, count + 1)]

print(result)
