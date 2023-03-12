# https://judge.softuni.org/Contests/Practice/Index/1739

while True:
    word = input()
    if word == "end":
        break
    print(f"{word} = {word[::-1]}")
