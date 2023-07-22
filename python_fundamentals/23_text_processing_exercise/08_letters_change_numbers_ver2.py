# https://judge.softuni.org/Contests/Compete/Index/1740#7

import re


def get_letter_position(letter): return 1 + ord(letter.lower()) - ord("a")


string = input()
pattern = r"([a-zA-z])(\d+)([a-zA-z])"

total_result = 0
matches = re.findall(pattern, string)
for front_letter, number_str, next_letter in matches:
    number = int(number_str)

    current_result = number
    if front_letter.isupper():
        current_result /= get_letter_position(front_letter)
    else:
        current_result *= get_letter_position(front_letter)

    if next_letter.isupper():
        current_result -= get_letter_position(next_letter)
    else:
        current_result += get_letter_position(next_letter)

    total_result += current_result

print(f"{total_result:.2f}")
