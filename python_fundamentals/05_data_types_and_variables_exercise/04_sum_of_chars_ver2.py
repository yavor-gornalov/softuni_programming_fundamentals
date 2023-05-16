# https://judge.softuni.org/Contests/Compete/Index/1722#3

number = int(input())
ascii_codes = [ord(input()) for _ in range(number)]

print(f"The sum equals: {sum(ascii_codes)}")
