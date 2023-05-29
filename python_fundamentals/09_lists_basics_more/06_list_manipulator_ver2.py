# https://judge.softuni.org/Contests/Practice/Index/1726#5

integers = [int(x) for x in input().split()]

while True:
    line = input()
    if line == "end":
        print(integers)
        break

    command, *tokens = line.split()
    if command == "exchange":
        index = int(tokens[0])
        if 0 <= index < len(integers):
            integers = integers[index + 1:] + integers[:index + 1]
        else:
            print("Invalid index")

    elif command in ["max", "min"]:
        even_odd = tokens[0]
        extreme_values = sorted([x for x in integers if x % 2 == (even_odd == "odd")], reverse=command == "max")
        if extreme_values:
            extreme_index = max([x for x in range(len(integers)) if integers[x] == extreme_values[0]])
            print(extreme_index)
        else:
            print("No matches")

    elif command in ["first", "last"]:
        count, even_odd = int(tokens[0]), tokens[1]
        if 0 < count <= len(integers):
            result = [x for x in integers if x % 2 == (even_odd == "odd")]
            print(result[:count]) if command == "first" else print(result[-count::])
        else:
            print("Invalid count")
