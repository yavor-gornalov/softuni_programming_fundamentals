# https://judge.softuni.org/Contests/Practice/Index/1737#8

n = int(input())
grades = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for name in grades:
    avg_grade = sum(grades[name]) / len(grades[name])
    if avg_grade >= 4.50:
        print(f"{name} -> {avg_grade:.2f}")
