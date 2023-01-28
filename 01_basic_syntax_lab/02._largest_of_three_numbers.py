# https://judge.softuni.org/Contests/Practice/Index/1718#1

def get_max(num1, num2):
    if num1 >= num2:
        result = num1
    else:
        result = num2
    return result


# main
a = int(input())
b = int(input())
c = int(input())

maximum = get_max(get_max(a, b), c)
print(maximum)
