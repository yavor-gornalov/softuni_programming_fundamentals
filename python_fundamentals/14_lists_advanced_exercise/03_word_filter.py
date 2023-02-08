# https://judge.softuni.org/Contests/Compete/Index/1731#2

even_length_words = [word for word in input().split(" ") if not len(word) % 2]
print("\n".join(even_length_words))
