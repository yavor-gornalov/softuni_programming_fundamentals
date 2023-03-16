# https://judge.softuni.org/Contests/Compete/Index/1740#3

text = input()
encrypted_list = [chr(ord(ch) + 3) for ch in text]
print("".join(encrypted_list))
