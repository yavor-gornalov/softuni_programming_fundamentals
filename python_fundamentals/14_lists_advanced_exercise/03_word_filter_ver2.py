# https://judge.softuni.org/Contests/Compete/Index/1731#2

even_length_words = [word for word in input().split() if len(word) % 2 == 0]
[print(word) for word in even_length_words]
