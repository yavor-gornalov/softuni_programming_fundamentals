# https://judge.softuni.org/Contests/Practice/Index/1721#5

year = int(input())

while True:
    year += 1
    happy_year = str(year)
    if len(set(happy_year)) == len(happy_year):
        print(happy_year)
        break
