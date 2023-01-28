# https://judge.softuni.org/Contests/Compete/Index/1719#5

def is_string_pure(string):
    is_pure = True
    pattern = ",._"
    for ch in pattern:
        if ch in string:
            is_pure = False
            break
    return is_pure


# main
n = int(input())

for _ in range(n):
    input_str = input()
    if is_string_pure(input_str):
        print(f"{input_str} is pure.")
    else:
        print(f"{input_str} is not pure!")
