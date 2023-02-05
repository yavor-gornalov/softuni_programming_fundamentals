# https://judge.softuni.org/Contests/Practice/Index/1729#3

def tribonacci(count):
    a, b, c = 0, 0, 1
    counter = 0
    while counter < count:
        print(c, end=' ')
        new_c = a + b + c
        a = b
        b = c
        c = new_c
        counter += 1
    print()


n = int(input())
tribonacci(n)
