# https://judge.softuni.org/Contests/Compete/Index/1740#8

text = input()

number, final_text = "", ""
result, prev = text[0], text[0]
for i in range(1, len(text)):
    ch = text[i]
    if not ch.isnumeric() and prev.isnumeric():
        final_text += result.upper() * int(number)
        number, result = "", ""
    if ch.isnumeric():
        number += ch
    else:
        result += ch

    prev = text[i]
else:
    final_text += result.upper() * int(number)

print(f"Unique symbols used: {len(set(final_text))}")
print(final_text)
