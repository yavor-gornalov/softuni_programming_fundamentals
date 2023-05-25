# https://judge.softuni.org/Contests/Practice/Index/1723#2

key = int(input())
number_of_lines = int(input())

text = [chr(ord(input()) + key) for _ in range(number_of_lines)]

print(*text, sep="")
