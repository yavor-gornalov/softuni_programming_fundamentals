# https://judge.softuni.org/Contests/Compete/Index/1719#3

def largest_divisible(divisor, boundary):
    result = 1
    for divisible in range(boundary, 0, -1):
        if divisible % divisor == 0:
            result = divisible
            break
    return result


# main
div = int(input())
bound = int(input())

res = largest_divisible(div, bound)

print(res)
