# https://judge.softuni.org/Contests/Compete/Index/1731#8

def merge(array, start_idx, end_idx):
    start_idx = max(0, start_idx)
    end_idx = min(len(array) - 1, end_idx)
    for idx in range(start_idx, end_idx):
        array[start_idx] += array.pop(start_idx + 1)

    return array


def divide(array, idx, parts):
    dividable_element = array[idx]
    slice_length = len(dividable_element) // parts

    new_elements = []
    for i in range(0, slice_length * (parts - 1), slice_length):
        new_elements.append(dividable_element[i:i + slice_length])
    new_elements.append(dividable_element[slice_length * (parts - 1):])
    array.pop(idx)

    return array[:idx] + new_elements + array[idx:]


commands = {
    "merge": merge,
    "divide": divide
}

strings = input().split()

line = input()
while not line == "3:1":
    command, *tokens = line.split()
    strings = commands[command](strings, *[int(t) for t in tokens])
    line = input()

print(" ".join(strings))
