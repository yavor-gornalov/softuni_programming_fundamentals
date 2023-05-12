# https://judge.softuni.org/Contests/Compete/Index/1719#6

while True:
    line = input()
    if line == "End":
        break
    elif line == "SoftUni":
        continue

    result = [ch * 2 for ch in line]
    print(*result, sep="")
