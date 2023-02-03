# https://judge.softuni.org/Contests/Compete/Index/1728#4

def evens(x): return not x % 2


seq = [int(x) for x in input().split()]
filtered_seq = filter(evens, seq)
res = []
for el in filtered_seq:
    res.append(el)

print(res)
