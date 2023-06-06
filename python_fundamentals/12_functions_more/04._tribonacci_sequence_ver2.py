# https://judge.softuni.org/Contests/Practice/Index/1729#3

"""
Time limit exceeded in judge system
"""


def recursive_tribonacci(n):
    if n < 1:
        return 0
    if n < 3:
        return 1
    return recursive_tribonacci(n - 1) + recursive_tribonacci(n - 2) + recursive_tribonacci(n - 3)


def tribonacci_sequence(n):
    return [recursive_tribonacci(i) for i in range(1, n + 1)]


number = int(input())
print(*tribonacci_sequence(number))
