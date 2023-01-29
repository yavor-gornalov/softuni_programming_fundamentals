# https://judge.softuni.org/Contests/Practice/Index/1723#3

n = int(input())
bracket_list = []
for _ in range(n):
    ch = input()
    if ch in "()":
        bracket_list.append(ch)

is_balanced = True
for i in range(len(bracket_list)):
    if i % 2 == 0 and bracket_list[i] == "(" or not i % 2 == 0 and bracket_list[i] == ")":
        is_balanced = True
    else:
        is_balanced = False
        break


if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
