# https://judge.softuni.org/Contests/Practice/Index/1726#1

indexes_sequence = [sum([int(x) for x in part]) for part in input().split()]
text = [x for x in input()]

message = [text.pop(idx % len(text)) for idx in indexes_sequence]

print("".join(message))
