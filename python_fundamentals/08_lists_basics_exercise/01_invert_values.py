# https://judge.softuni.org/Contests/Compete/Index/1725#0

num_list = list(input().split(" "))

opposite_list = []
for num in num_list:
    opposite_list.append(-1 * int(num))

print(opposite_list)
