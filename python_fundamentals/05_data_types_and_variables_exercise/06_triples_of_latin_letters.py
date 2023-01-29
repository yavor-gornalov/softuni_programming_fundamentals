# https://judge.softuni.org/Contests/Compete/Index/1722#5

n = int(input())
for i in range(ord("a"), ord("a") + n):
    for j in range(ord("a"), ord("a") + n):
        for k in range(ord("a"), ord("a") + n):
            print(f"{chr(i)}{chr(j)}{chr(k)}")
