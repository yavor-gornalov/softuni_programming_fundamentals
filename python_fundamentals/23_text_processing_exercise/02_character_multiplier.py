# https://judge.softuni.org/Contests/Compete/Index/1740#1

first_str, second_str = input().split()

first_len = len(first_str)
second_len = len(second_str)
short_idx = min(first_len, second_len)
long_idx = max(first_len, second_len)

total_sum = 0
for i in range(long_idx):
    if i < short_idx:
        total_sum += ord(first_str[i]) * ord(second_str[i])
        if long_idx == short_idx:
            continue
    else:
        if first_len > second_len:
            total_sum += ord(first_str[i])
        else:
            total_sum += ord(second_str[i])

print(total_sum)
