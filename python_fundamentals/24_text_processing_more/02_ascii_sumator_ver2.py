# https://judge.softuni.org/Contests/Practice/Index/1741#1

first = ord(input())
second = ord(input())
text = input()

result = 0
for ch in text:
    if first < ord(ch) < second:
        result += ord(ch)

print(result)
