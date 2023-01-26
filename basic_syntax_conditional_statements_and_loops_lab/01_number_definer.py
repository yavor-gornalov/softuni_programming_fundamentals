# https://judge.softuni.org/Contests/Practice/Index/1718#0

def number_definer(number):
    result = "zero"

    if number > 0:
        if number < 1:
            result = "small positive"
        elif number < 1000000:
            result = "positive"
        else:
            result = "large positive"
    elif number < 0:
        if number > -1:
            result = "small negative"
        elif number > -1000000:
            result = "negative"
        else:
            result = "large negative"

    return result


# main
num = float(input())

print(number_definer(num))
