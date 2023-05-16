# https://judge.softuni.org/Contests/Compete/Index/1722#5

offset = int(input())

start = ord("a")
end = start + offset

letters = [chr(i) for i in range(start, end)]

for i in letters:
    for j in letters:
        for k in letters:
            print(i, j, k, sep="")
