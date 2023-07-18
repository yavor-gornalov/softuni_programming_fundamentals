# https://judge.softuni.org/Contests/Compete/Index/1737#2

countries = input().split(", ")
capitals = input().split(", ")

[print(f"{countries[i]} -> {capitals[i]}") for i in range(len(countries))]
