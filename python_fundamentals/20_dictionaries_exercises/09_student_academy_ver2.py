# https://judge.softuni.org/Contests/Compete/Index/1737#8

students = {}
students_count = int(input())
for _ in range(students_count):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade:.2f}")
