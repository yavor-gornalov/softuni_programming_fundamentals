# https://judge.softuni.org/Contests/Practice/Index/2302#1

import re

pattern = r"(?P<emoji>(?P<sep>\:\:|\*\*)(?P<text>[A-Z][a-z]{2,})(?P=sep))"
regex = re.compile(pattern)

line = input()
matches = regex.finditer(line)

cool_threshold = 1
for ch in line:
    if ch.isnumeric():
        cool_threshold *= int(ch)
top_emojis, counter = [], 0
for match in matches:
    emoji = match.group("emoji")
    text = match.group("text")
    current_threshold = sum([ord(ch) for ch in text])
    if current_threshold >= cool_threshold:
        top_emojis.append(emoji)
    counter += 1

print(f"Cool threshold: {cool_threshold}\n"
      f"{counter} emojis found in the text. The cool ones are:")
print('\n'.join(top_emojis))
