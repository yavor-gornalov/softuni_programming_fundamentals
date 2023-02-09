# https://judge.softuni.org/Contests/Compete/Index/1731#8
# TODO: check out code in Softuni Judge system


def merge(seq, start, end):
    merged_el = [seq[ind] for ind in range(len(seq)) if start <= ind <= end]
    seq = [el for el in seq if el not in merged_el]
    seq.insert(start, "".join(merged_el).replace(",", ""))
    return seq


def divide(seq, ind, cnt):
    current_el = seq[ind]
    substrings_length = len(current_el) // cnt
    split_el = []
    while len(current_el) >= 2 * substrings_length:
        split_el.append(current_el[:substrings_length])
        current_el = current_el[substrings_length:]
    else:
        split_el.append(current_el)
    seq.pop(ind)
    seq = seq[:ind] + split_el + seq[ind:]
    return seq


data = input().split()

command = input()
while not command == "3:1":
    tokens = command.split()
    command = tokens[0]

    if command == "merge":
        stat_index = int(tokens[1])
        end_index = int(tokens[2])
        data = merge(seq=data, start=stat_index, end=end_index)

    elif command == "divide":
        index = int(tokens[1])
        substrings_count = int(tokens[2])
        data = divide(seq=data, ind=index, cnt=substrings_count)

    command = input()

print(" ".join(data))
