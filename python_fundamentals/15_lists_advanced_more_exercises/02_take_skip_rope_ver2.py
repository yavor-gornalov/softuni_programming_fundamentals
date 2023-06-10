# https://judge.softuni.org/Contests/Practice/Index/1732#1

input_string = input()
non_number_list = [ch for ch in input_string if not ch.isnumeric()]
number_list = [int(n) for n in input_string if n not in non_number_list]

take_list, skip_list = [], []
for index, value in enumerate(number_list):
    if not index % 2:
        take_list.append(number_list[index])  # evens
    else:
        skip_list.append(number_list[index])  # odds

result = []
m, n = 0, 0
for i in range(len(take_list)):
    n = m + take_list[i]
    result += non_number_list[m:n]
    m = n + skip_list[i]

print("".join(result))
