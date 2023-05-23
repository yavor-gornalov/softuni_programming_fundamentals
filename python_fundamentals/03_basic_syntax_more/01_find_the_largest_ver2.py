# https://judge.softuni.org/Contests/Practice/Index/1720#0

number = input()

digits = [d for d in number]
biggest_number = ''.join(sorted(digits, reverse=True))

print(biggest_number)
