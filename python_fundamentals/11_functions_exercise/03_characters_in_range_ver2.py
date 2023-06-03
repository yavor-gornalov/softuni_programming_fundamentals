# https://judge.softuni.org/Contests/Compete/Index/1728#2

def print_chars_between(start, end):
    set_of_chars = [chr(x) for x in range(ord(start) + 1, ord(end))]
    print(" ".join(set_of_chars))


first_char, second_char = [input() for _ in range(2)]
print_chars_between(first_char, second_char)
