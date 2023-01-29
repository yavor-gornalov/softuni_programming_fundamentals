# https://judge.softuni.org/Contests/Practice/Index/1724#4

n = int(input())

number_string = []
for _ in range(n):
    number = int(input())
    number_string.append(number)
command = input()

filtered_string = []
if command == "even":
    for number in number_string:
        if number % 2 == 0:
            filtered_string.append(number)
elif command == "odd":
    for number in number_string:
        if not number % 2 == 0:
            filtered_string.append(number)
elif command == "negative":
    for number in number_string:
        if number < 0:
            filtered_string.append(number)
elif command == "positive":
    for number in number_string:
        if not number < 0:
            filtered_string.append(number)

print(filtered_string)
