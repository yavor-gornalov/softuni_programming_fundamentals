# https://judge.softuni.org/Contests/Compete/Index/1737#7

courses = {}

line = input()
while line != "end":
    course_name, student_name = line.split(" : ")
    if course_name not in courses:
        courses[course_name] = {"count": 0, "students": []}
    courses[course_name]["count"] += 1
    courses[course_name]["students"].append(student_name)
    line = input()

for course, data in courses.items():
    print(f'{course}: {data["count"]}')
    for student in data["students"]:
        print(f'-- {student}')
