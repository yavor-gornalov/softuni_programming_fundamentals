# https://judge.softuni.org/Contests/Compete/Index/1728#6

def print_sequence_characteristics(seq):
    print(f"The minimum number is {min(seq)}\n"
          f"The maximum number is {max(seq)}\n"
          f"The sum number is: {sum(seq)}")


# main
numbers = [int(x) for x in input().split()]
print_sequence_characteristics(numbers)
