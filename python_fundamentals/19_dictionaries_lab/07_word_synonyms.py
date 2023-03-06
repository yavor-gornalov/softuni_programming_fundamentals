# https://judge.softuni.org/Contests/Practice/Index/1736#6

n = int(input())

synonyms = {}
for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for key in synonyms:
    print(f"{key} - {', '.join(synonyms[key])}")
