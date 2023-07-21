# https://judge.softuni.org/Contests/Compete/Index/1740#6

text = input()
new_text = ""

strength = 0
idx = 0
while idx < len(text):
    idx += 1
    prev = text[idx - 1]
    if prev == ">":
        start_idx = idx
        while idx < len(text) and text[idx].isdigit():
            idx += 1
            strength -= 1
        strength += int(text[start_idx: idx])
        new_text += prev
    else:
        if not strength:
            new_text += prev
        else:
            strength -= 1

print(new_text)
