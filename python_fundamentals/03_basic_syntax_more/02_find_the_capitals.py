# https://judge.softuni.org/Contests/Practice/Index/1720#1

user_string = input()

positions = []
for i, ch in enumerate(user_string):
    if ch.isupper():
        positions.append(i)

print(positions)
