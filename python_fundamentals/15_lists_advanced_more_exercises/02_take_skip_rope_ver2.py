# https://judge.softuni.org/Contests/Practice/Index/1732#1

hidden_message = input()

text, take_list, skip_list = [], [], []

is_even_idx = True  # idx starts always from 0, zero is even
for char in hidden_message:
    if char.isnumeric():
        take_list.append(int(char)) if is_even_idx else skip_list.append(int(char))
        is_even_idx = not is_even_idx
    else:
        text.append(char)

message = []
current_idx = 0
for i in range(len(take_list)):
    take_count = take_list[i]
    skip_count = skip_list[i]
    message.extend(text[current_idx:current_idx + take_count])
    current_idx += take_count + skip_count

print(*message, sep="")
