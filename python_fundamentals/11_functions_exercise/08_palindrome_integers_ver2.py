# https://judge.softuni.org/Contests/Compete/Index/1728#7

def is_palindrome(num):
    return num == num[::-1]


print(*[is_palindrome(x) for x in input().split(", ")], sep="\n")
