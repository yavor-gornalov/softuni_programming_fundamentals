# https://judge.softuni.org/Contests/Practice/Index/2474#2

numbers = [int(x) for x in input().split()]

average = sum(numbers) / len(numbers)

top_numbers = sorted([n for n in numbers if n > average], reverse=True)[:5]

print(*top_numbers, sep=" ") if top_numbers else print("No")
