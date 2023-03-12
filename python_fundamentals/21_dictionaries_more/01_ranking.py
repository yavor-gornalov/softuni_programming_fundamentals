# https://judge.softuni.org/Contests/Practice/Index/1738#0

contests_by_pass = {}
users_by_contests = {}
users_by_points = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contests_by_pass[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    args = command.split("=>")
    contest = args[0]
    password = args[1]
    username = args[2]
    points = int(args[3])

    if contest not in contests_by_pass or password != contests_by_pass[contest]:
        continue
    if username not in users_by_contests:
        users_by_contests[username] = {}
    if contest not in users_by_contests[username]:
        users_by_contests[username][contest] = points
    else:
        users_by_contests[username][contest] = max(users_by_contests[username][contest], points)

for user, contest in users_by_contests.items():
    users_by_points[user] = sum(users_by_contests[user].values())

top_user = max(users_by_points, key=lambda k: users_by_points[k])
print(f"Best candidate is {top_user} with total {users_by_points[top_user]} points.")
print("Ranking:")

users_by_name = {k: users_by_contests[k] for k in sorted(users_by_contests)}

for user, contest in users_by_name.items():
    print(user)
    user_courses = dict(sorted(contest.items(), key=lambda x: -x[1]))
    for course, points in user_courses.items():
        print(f"#  {course} -> {points}")
