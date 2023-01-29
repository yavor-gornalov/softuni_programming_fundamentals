# https://judge.softuni.org/Contests/Practice/Index/1721#4

n = int(input())

for i in range(1, n + 1):
    num = str(i)
    sum_digits = 0
    for ch in num:
        sum_digits += int(ch)

    is_special = False
    if sum_digits in [5, 7, 11]:
        is_special = True

    print(f"{i} -> {is_special}")
