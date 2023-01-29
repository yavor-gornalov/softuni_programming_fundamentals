# https://judge.softuni.org/Contests/Compete/Index/1725#1

factor = int(input())
count = int(input())

result = []
for i in range(1, count + 1):
    result.append(i * factor)

print(result)
