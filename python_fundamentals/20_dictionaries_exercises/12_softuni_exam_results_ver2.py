# https://judge.softuni.org/Contests/Compete/Index/1737#11

def submit_result(username, language, points, students, submissions):
    current_points = int(points)
    if username not in students:
        students[username] = {language: current_points}
    elif language in students[username]:
        students[username] = {language: max(students[username][language], current_points)}

    if language not in submissions:
        submissions[language] = 0

    submissions[language] += 1


def ban_user(username, command, banned_list):
    banned_list.add(username)


students = {}
submissions = {}
banned_list = set()

line = input()
while line != "exam finished":
    args = line.split("-")

    if "banned" in line:
        ban_user(*args, banned_list)
    else:
        submit_result(*args, students, submissions)

    line = input()

print("Results:")
for student, data in students.items():
    if student not in banned_list:
        for points in data.values():
            print(f"{student} | {points}")

print("Submissions:")
for language, submissions_count in submissions.items():
    print(f"{language} - {submissions_count}")
