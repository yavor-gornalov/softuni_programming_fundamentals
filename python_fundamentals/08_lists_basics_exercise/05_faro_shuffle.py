# https://judge.softuni.org/Contests/Compete/Index/1725#4

cards = list(input().split(" "))
shuffles = int(input())

for _ in range(shuffles):
    deck_1 = cards[1:len(cards) // 2]
    deck_2 = cards[len(cards) // 2:len(cards) - 1]
    temp = list()

    for i in range(len(deck_1)):
        temp.append(deck_2[i])
        temp.append(deck_1[i])

    cards[1: len(cards) - 1] = temp

print(cards)
