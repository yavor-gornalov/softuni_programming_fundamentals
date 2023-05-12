# https://judge.softuni.org/Contests/Compete/Index/1719#5

pattern = ",._"
number_of_strings = int(input())

for _ in range(number_of_strings):
    is_pure = True
    line = input()
    for symbol in pattern:
        if symbol in line:
            is_pure = False
            break

    message = f"{line} is pure." if is_pure else f"{line} is not pure!"
    print(message)
