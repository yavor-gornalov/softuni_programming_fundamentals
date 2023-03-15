# https://judge.softuni.org/Contests/Compete/Index/1740#0
from string import ascii_letters, digits

usernames = input().split(", ")

allowed_symbols = ascii_letters + digits + "_" + "-"

for username in usernames:
    if not 3 <= len(username) <= 16:
        continue
    if not all([ch in allowed_symbols for ch in username]):
        continue
    print(username)
