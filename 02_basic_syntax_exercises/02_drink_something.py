# https://judge.softuni.org/Contests/Compete/Index/1719#1

age = int(input())
drink = ''
if age <= 14:
    drink = "toddy"
elif age <= 18:
    drink = "coke"
elif age <= 21:
    drink = "beer"
else:
    drink = "whisky"

print(f"drink {drink}")
