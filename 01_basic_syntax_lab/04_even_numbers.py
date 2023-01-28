# https://judge.softuni.org/Contests/Practice/Index/1718#3

def is_odd(num):
    res = False
    if not num % 2 == 0:
        res = True
    return res


# main
n = int(input())

for _ in range(n):
    number = int(input())
    if is_odd(number):
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")
