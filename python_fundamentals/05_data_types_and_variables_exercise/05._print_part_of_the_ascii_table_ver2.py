# https://judge.softuni.org/Contests/Compete/Index/1722#4

start, end = [int(input()) for _ in range(2)]

chars = [chr(i) for i in range(start, end + 1)]
print(*chars, sep=" ")
