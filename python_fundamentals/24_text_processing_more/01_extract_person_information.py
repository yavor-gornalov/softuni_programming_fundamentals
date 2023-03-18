# https://judge.softuni.org/Contests/Practice/Index/1741#0

n = int(input())

for _ in range(n):
    person_info = input().split()
    name, age = None, None
    for word in person_info:
        if "@" in word and "|":
            name = word[word.find("@") + 1: word.find("|")]
        if "#" in word and "*" in word:
            age = word[word.find("#") + 1: word.find("*")]
    print(f"{name} is {age} years old.")
