# https://judge.softuni.org/Contests/Compete/Index/1731#1

line = input()
current_version = int(line.replace(".", ""))
current_version += 1

next_version = []
while current_version:
    next_version.insert(0, current_version % 10)
    current_version //= 10

print(*next_version, sep=".")
