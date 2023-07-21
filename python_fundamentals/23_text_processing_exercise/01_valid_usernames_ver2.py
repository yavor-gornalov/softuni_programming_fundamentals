# https://judge.softuni.org/Contests/Compete/Index/1740#0

from string import ascii_letters, digits


def is_username_valid(user):
    allowed_symbols = ascii_letters + digits + "_" + "-"

    if len(user) < 3 or len(user) > 16:
        return False

    for symbol in user:
        if symbol not in allowed_symbols:
            return False

    if " " in user:
        return False

    return True


usernames = input().split(", ")
[print(user) for user in usernames if is_username_valid(user)]
