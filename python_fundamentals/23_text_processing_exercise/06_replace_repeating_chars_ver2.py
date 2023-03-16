# https://judge.softuni.org/Contests/Compete/Index/1740#5

text = input()

clear_text = text[0]
for ch in text:
    if ch == clear_text[-1]:
        continue
    clear_text += ch

print(clear_text)
