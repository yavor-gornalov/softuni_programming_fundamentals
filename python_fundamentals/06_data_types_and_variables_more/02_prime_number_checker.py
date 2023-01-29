# https://judge.softuni.org/Contests/Practice/Index/1723#1

num = int(input())
is_prime = True
if num in [0, 1]:
    is_prime = False
else:
    for divider in range(2, num//2 + 1):
        if num % divider == 0:
            is_prime = False

print(is_prime)

