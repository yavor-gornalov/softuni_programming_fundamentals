# https://judge.softuni.org/Contests/Practice/Index/1718#6

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")
    print()

