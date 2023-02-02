# https://judge.softuni.org/Contests/Practice/Index/1726#5

elements = [int(x) for x in input().split()]


def max_even(seq, is_maximum=True, is_even=True):
    if is_maximum:
        for num in sorted(seq, reverse=True):
            if is_even:
                if not num % 2:
                    return num
            elif not is_even:
                if num % 2:
                    return num
    elif not is_maximum:
        for num in sorted(seq, reverse=False):
            if is_even:
                if not num % 2:
                    return num
            elif not is_even:
                if num % 2:
                    return num


def first_count_even(seq, is_first, is_even, cnt):
    res = []
    for num in seq:
        if is_even:
            if not num % 2:
                res.append(num)
        if not is_even:
            if num % 2:
                res.append(num)
    if is_first:
        return res[0:cnt]
    elif not is_first:
        return res[-cnt::]


command = input()
while not command == "end":
    tokens = command.split()
    command = tokens[0]
    if command == "exchange":
        index = int(tokens[1])
        if 0 <= index < len(elements):
            elements = elements[index + 1:] + elements[:index + 1]
        else:
            print("Invalid index")

    elif command in ["max", 'min']:
        subcommand = tokens[1]
        maximum = command == "max"
        even = subcommand == "even"
        result = max_even(elements, is_maximum=maximum, is_even=even)
        if result or result == 0:
            for i in range(len(elements) - 1, -1, - 1):
                if elements[i] == result:
                    print(i)
                    break
        else:
            print("No matches")

    elif command in ["first", "last"]:
        count = int(tokens[1])
        subcommand = tokens[2]
        if 0 < count <= len(elements):
            first = command == "first"
            even = subcommand == "even"
            result = first_count_even(elements, is_first=first, is_even=even, cnt=count)
            print(result)
        else:
            print("Invalid count")

    command = input()
else:
    print(elements)
