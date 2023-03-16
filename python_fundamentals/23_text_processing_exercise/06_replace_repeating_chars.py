# https://judge.softuni.org/Contests/Compete/Index/1740#5

text = input()

clear_text = ""
idx, length = 0, 1
while True:
    if idx + length >= len(text):
        clear_text += text[idx]
        break
    if text[idx + length] == text[idx]:
        length += 1
        continue
    clear_text += text[idx]
    idx += length
    length = 1

print(clear_text)
