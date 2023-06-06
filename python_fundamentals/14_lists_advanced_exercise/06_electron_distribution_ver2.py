# https://judge.softuni.org/Contests/Compete/Index/1731#5

number_of_electrons = int(input())

filled_shells = []
shell_number = 1
while number_of_electrons > 0:
    current_shell_size = 2 * shell_number ** 2
    filled_shells.append(min(number_of_electrons, current_shell_size))
    number_of_electrons -= current_shell_size
    shell_number += 1

print(filled_shells)
