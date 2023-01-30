# https://judge.softuni.org/Contests/Compete/Index/1725#5

integers = list(map(int, input().split(" ")))
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    min_value = min(integers)
    min_index = integers.index(min_value)
    integers.pop(min_index)

print(', '.join(map(str, integers)))
