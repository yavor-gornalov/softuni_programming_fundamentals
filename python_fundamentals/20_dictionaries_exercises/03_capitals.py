# https://judge.softuni.org/Contests/Practice/Index/1737#2

countries = [x for x in input().split(", ")]
capitols = [y for y in input().split(", ")]

info = {countries[i]: capitols[i] for i in range(len(countries))}

[print(f"{key} -> {info[key]}") for key in info]
