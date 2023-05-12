# https://judge.softuni.org/Contests/Compete/Index/1719#9

first_string = input()
second_string = input()

for idx in range(0, len(first_string)):
    if first_string[idx] == second_string[idx]:
        continue
    print(second_string[:idx + 1], first_string[idx + 1:], sep="")
