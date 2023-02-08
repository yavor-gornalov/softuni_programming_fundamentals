# https://judge.softuni.org/Contests/Compete/Index/1731#5

number_of_electrons = int(input())

shell_number = 1
shell_list = []
while True:
    shell_capacity = 2 * shell_number ** 2
    if shell_capacity >= number_of_electrons:
        shell_list.append(number_of_electrons)
        break
    number_of_electrons -= shell_capacity
    shell_list.append(shell_capacity)
    shell_number += 1

print(shell_list)
