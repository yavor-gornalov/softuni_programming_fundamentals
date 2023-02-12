# https://judge.softuni.org/Contests/Practice/Index/1732#1
# TODO: not finished

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
for i in range(len(take_list)):
    m, n = take_list[i], skip_list[i]
    result += input_string[:m]
    input_string = input_string[(m + n):]

print("".join(result))
