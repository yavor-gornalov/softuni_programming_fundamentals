# https://judge.softuni.org/Contests/Compete/Index/1725#3

number_string = input().split(", ")
beggars = int(input())

beggars_sum_list = []
for beggar in range(beggars):
    current_beggar_numbers = []
    for i in range(beggar, len(number_string), beggars):
        current_beggar_numbers.append(int(number_string[i]))
    current_sum = sum(current_beggar_numbers)
    beggars_sum_list.append(current_sum)

print(beggars_sum_list)
