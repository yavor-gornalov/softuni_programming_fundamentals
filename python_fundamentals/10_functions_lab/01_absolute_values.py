# https://judge.softuni.org/Contests/Practice/Index/1727#0

def absolute_values(seq):
    res = []
    for el in seq:
        res.append(abs(el))
    return res


sequence = [float(x) for x in input().split()]
print(absolute_values(seq=sequence))
