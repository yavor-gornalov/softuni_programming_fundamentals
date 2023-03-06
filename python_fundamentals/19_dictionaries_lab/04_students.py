# https://judge.softuni.org/Contests/Practice/Index/1736#3

courses = {}
while True:
    command = input()
    if ":" not in command:
        break
    command_args = command.split(":")
    student_name = command_args[0]
    student_id = int(command_args[1])
    course_key = command_args[2]
    if course_key not in courses:
        courses[course_key] = {}
    courses[course_key][student_id] = student_name

search_course = command.lower().replace("_", " ")

if search_course in courses:
    for student_id, student_name in courses[search_course].items():
        print(f"{student_name} - {student_id}")
