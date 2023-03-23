# https://judge.softuni.org/Contests/Practice/Index/1744#0

import re

racers = input().split(", ")
racers_distance = dict.fromkeys(racers, 0)

letters_pattern = r"[A-Z]|[a-z]+"
letters_regex = re.compile(letters_pattern)
digits_pattern = r"\d"
digits_regex = re.compile(digits_pattern)

while True:
    line = input()
    if line == "end of race":
        break
    name = "".join(re.findall(letters_regex, line))
    digits = re.findall(digits_regex, line)
    current_distance = sum([int(digit) for digit in digits])
    if name in racers_distance:
        racers_distance[name] += current_distance

race_winners = [x[0] for x in sorted(racers_distance.items(), key=lambda x: -x[1])]
print(f"1st place: {race_winners[0]}\n"
      f"2nd place: {race_winners[1]}\n"
      f"3rd place: {race_winners[2]}")
