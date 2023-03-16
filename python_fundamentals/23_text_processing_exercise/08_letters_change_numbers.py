# https://judge.softuni.org/Contests/Compete/Index/1740#7

line = input().strip().split()


def get_letter_position(letter): return 1 + ord(letter.lower()) - ord("a")


total_sum = 0
for string in line:
    current_result = 0
    number = int(string[1:len(string) - 1])

    first_letter = string[0]
    first_operand = get_letter_position(first_letter)
    if first_letter.isupper():
        current_result = number / first_operand
    else:
        current_result = number * first_operand

    second_letter = string[-1]
    second_operand = get_letter_position(second_letter)
    if second_letter.isupper():
        current_result -= second_operand
    else:
        current_result += second_operand

    total_sum += current_result

print(f"{total_sum:.2f}")
