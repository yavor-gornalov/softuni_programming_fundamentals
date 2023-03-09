# https://judge.softuni.org/Contests/Practice/Index/1737#7

courses = {}

while True:
    command = input()
    if command == "end":
        break
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
