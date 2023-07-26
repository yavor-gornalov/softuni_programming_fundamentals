# https://judge.softuni.org/Contests/Practice/Index/2307#1

import re


def find_word_pairs(pattern, text):
    words = re.findall(pattern, text)
    mirror_words = []
    for sep, first, second in words:
        if first == second[::-1]:
            mirror_words.append(f"{first} <=> {second}")
    return words, mirror_words


def print_result(words, mirror_words):
    word_pairs = len(words)
    if not word_pairs:
        print("No word pairs found!")
    else:
        print(f"{word_pairs} word pairs found!")
    if not mirror_words:
        print("No mirror words!")
    else:
        print(f"The mirror words are:\n{', '.join(x for x in mirror_words)}")


words_pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

line = input()
all_words, word_pairs = find_word_pairs(words_pattern, line)
print_result(all_words, word_pairs)
