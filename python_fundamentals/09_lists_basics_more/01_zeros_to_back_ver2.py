# https://judge.softuni.org/Contests/Practice/Index/1726#0

integers = [int(x) for x in input().split(", ")]

index, limit = 0, len(integers)
while index < limit:
    if integers[index] == 0:
        integers.append(integers.pop(index))
        limit -= 1
    else:
        index += 1

print(integers)
