# https://judge.softuni.org/Contests/Compete/Index/1725#3

integers = [int(x) for x in input().split(", ")]
number_of_beggars = int(input())
beggars_amount = []

for i in range(number_of_beggars):
    beggars_amount.append([integers[num] for num in range(i, len(integers), number_of_beggars)])

print([sum(amount) for amount in beggars_amount])
