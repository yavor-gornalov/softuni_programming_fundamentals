# https://judge.softuni.org/Contests/Compete/Index/1740#5

text = input()
filtered_text = text[0]

for char in text:
    if char != filtered_text[-1]:
        filtered_text += char

print(filtered_text)
