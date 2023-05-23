# https://judge.softuni.org/Contests/Practice/Index/1720#1

text = input()
capitals = [idx for idx, letter in enumerate(text) if letter.isupper()]
print(capitals)
