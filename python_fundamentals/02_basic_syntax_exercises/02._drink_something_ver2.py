# https://judge.softuni.org/Contests/Compete/Index/1719#1

person_age = int(input())

drink = "whisky"
if person_age <= 14:
    drink = "toddy"
elif person_age <= 18:
    drink = "coke"
elif person_age <= 21:
    drink = "beer"

print(f"drink {drink}")
