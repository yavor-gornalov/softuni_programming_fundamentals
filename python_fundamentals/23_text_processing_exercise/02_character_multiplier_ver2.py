# https://judge.softuni.org/Contests/Compete/Index/1740#1

first, second = input().split()

result = 0
for idx in range(min(len(first), len(second))):
    result += ord(first[idx]) * ord(second[idx])

for i in range(idx + 1, len(first)):
    result += ord(first[i])

for i in range(idx + 1, len(second)):
    result += ord(second[i])

print(result)
