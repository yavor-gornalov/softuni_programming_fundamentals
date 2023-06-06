# https://judge.softuni.org/Contests/Compete/Index/1731#6

groups = {}
numbers = [int(x) for x in input().split(", ")]

current_group = 10
while numbers:
    if current_group not in groups:
        current_nums = [num for num in numbers if num <= current_group]
        groups[current_group] = [num for num in numbers if num <= current_group]
        [numbers.pop(numbers.index(num)) for num in current_nums]
    current_group += 10

[print(f"Group of {group_key}'s: {nums}") for group_key, nums in groups.items()]
