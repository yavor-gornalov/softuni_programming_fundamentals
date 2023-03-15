# https://judge.softuni.org/Contests/Compete/Index/1740#2

def reverse_search(seq, symbol):
    length = 0
    while True:
        ch = path[len(seq) - length - 1]
        if ch == symbol:
            break
        length += 1
    return length


path = input()

slash_idx = reverse_search(path, "\\")
dot_idx = reverse_search(path, ".")

print(f"File name: {path[-slash_idx:-dot_idx - 1:]}\n"
      f"File extension: {path[-dot_idx::]}")
