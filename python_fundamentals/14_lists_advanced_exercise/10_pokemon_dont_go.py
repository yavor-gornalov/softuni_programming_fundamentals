# TODO: https://judge.softuni.org/Contests/Compete/Index/1731#9
# TODO: check out code in Softuni Judge system


sequence = [int(x) for x in input().split()]
sum_removed_elements = 0
while not sequence == []:
    index = int(input())
    if index < 0:
        value = sequence[0]
        sequence[0] = sequence[-1]
    elif index <= len(sequence) - 1:
        value = sequence.pop(index)
    else:
        value = sequence[-1]
        sequence[-1] = sequence[0]

    sequence = [x + value if x <= value else x - value for x in sequence]
    sum_removed_elements += value

print(sum_removed_elements)
