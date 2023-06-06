# https://judge.softuni.org/Contests/Compete/Index/1731#0

substings = input().split(", ")
words = input().split(", ")

matches = []
for substing in substings:
    for word in words:
        if substing in word and substing not in matches:
            matches.append(substing)

print(matches)
