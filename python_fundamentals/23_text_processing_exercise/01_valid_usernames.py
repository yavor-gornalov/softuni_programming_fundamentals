# https://judge.softuni.org/Contests/Compete/Index/1740#0

usernames = input().split(", ")

for username in usernames:
    is_valid = True
    if not 3 <= len(username) <= 16:
        is_valid = False
    for symbol in username:
        if not (symbol.isalnum() or symbol == "_" or symbol == "-"):
            is_valid = False
            break
    if is_valid:
        print(username)
