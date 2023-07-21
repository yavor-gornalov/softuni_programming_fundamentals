# https://judge.softuni.org/Contests/Compete/Index/1740#4

text = input()

while ":" in text:
    idx = text.find(":")
    text = text.replace(":", "", 1)
    if text[idx]:
        print(":" + text[idx])
