# https://judge.softuni.org/Contests/Practice/Index/1726#1

num_sequence = input().split()
string = list(input())
message = str()
for num in num_sequence:
    index = 0
    for digit in num:
        index += int(digit)

    max_index = len(string) - 1
    if index > max_index:
        index = int(index % max_index - 1)
    message += string[index]
    string.pop(index)

print(message)
