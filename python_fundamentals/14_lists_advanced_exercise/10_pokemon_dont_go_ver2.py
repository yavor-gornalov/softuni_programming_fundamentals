# https://judge.softuni.org/Contests/Compete/Index/1731#9

sequence = [int(x) for x in input().split()]
sum_removed_elements = 0

while sequence:
    idx = int(input())
    if idx < 0:
        value = sequence[0]
        sequence[0] = sequence[-1]
    elif idx > len(sequence) - 1:
        value = sequence[-1]
        sequence[-1] = sequence[0]
    else:
        value = sequence.pop(idx)
    sequence = [ele + value if ele <= value else ele - value for ele in sequence]
    sum_removed_elements += value

print(sum_removed_elements)
