# https://judge.softuni.org/Contests/Compete/Index/1728#6

def minimum_number(seq): return min(seq)


def maximum_number(seq): return max(seq)


def sum_numbers(seq): return sum(seq)


# main
sequence = [int(x) for x in input().split()]

print(f"The minimum number is {minimum_number(sequence)}\n"
      f"The maximum number is {maximum_number(sequence)}\n"
      f"The sum number is: {sum_numbers(sequence)}")
