# https://judge.softuni.org/Contests/Compete/Index/1740#1

first_str, second_str = input().split()

first_len, second_len = len(first_str), len(second_str)
min_len = min(first_len, second_len)

total_sum = 0
for i in range(min_len):
    total_sum += ord(first_str[i]) * ord(second_str[i])
for i in range(min_len, first_len):
    total_sum += ord(first_str[i])
for i in range(min_len, second_len):
    total_sum += ord(second_str[i])

print(total_sum)
