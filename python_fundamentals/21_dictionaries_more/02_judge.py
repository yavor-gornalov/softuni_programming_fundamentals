# https://judge.softuni.org/Contests/Practice/Index/1738#1

users_contests_points = {}
contests_users = {}

while True:
    command = input()
    if command == "no more time":
        break
    args = command.split(" -> ")
    username, contest, points = args[0], args[1], int(args[2])
    if username not in users_contests_points:
        users_contests_points[username] = {}
    if contest not in contests_users:
        contests_users[contest] = []
    if username not in contests_users[contest]:
        contests_users[contest].append(username)
    if contest not in users_contests_points:
        users_contests_points[username][contest] = points
    else:
        users_contests_points[username][contest] = max(users_contests_points[username][contest], points)

for course, users in contests_users.items():
    print(f"{course}: {len(users)} participants")
    course_users = {user: users_contests_points[user][course] for user in users}
    course_users_sorted = dict(sorted(course_users.items(), key=lambda x: (-x[1], x[0])))
    for idx, user in enumerate(course_users_sorted, 1):
        print(f"{idx}. {user} <::> {course_users_sorted[user]}")

individual_stats = {usr: sum(pts.values()) for usr, pts in users_contests_points.items()}
individual_stats_sorted = dict(sorted(individual_stats.items(), key=lambda x: (-x[1], x[0])))
print("Individual standings:")
for i, (user, points) in enumerate(individual_stats_sorted.items(), 1):
    print(f"{i}. {user} -> {points}")
