# https://judge.softuni.org/Contests/Practice/Index/1727#2

from decimal import Decimal


def calc(a, b, operation):
    result = None
    if operation == "multiply":
        result = a * b
    elif operation == "divide":
        if not b == 0:
            result = Decimal(a / b)
    elif operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b

    return result


action = input()
first_num = int(input())
second_num = int(input())

print(calc(operation=action, a=first_num, b=second_num))
