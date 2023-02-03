# https://judge.softuni.org/Contests/Practice/Index/1727#6

def rounding(seq):
    rounded_seq = []
    for el in seq:
        rounded_seq.append(round(el))
    return rounded_seq


sequence = [float(x) for x in input().split()]
print(rounding(seq=sequence))
