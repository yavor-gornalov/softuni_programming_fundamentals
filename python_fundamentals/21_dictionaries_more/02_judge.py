# https://judge.softuni.org/Contests/Practice/Index/1738#1

contests_users = {}
user_stats = {}

while True:
    command = input()
    if command == "no more time":
        break
    args = command.split(" -> ")
    username, contest, points = args[0], args[1], int(args[2])
    if contest not in contests_users:
        contests_users[contest] = {}
    if username not in contests_users[contest]:
        contests_users[contest][username] = points
    else:
        contests_users[contest][username] = max(contests_users[contest][username], points)

    if username not in user_stats:
        user_stats[username] = {}
    if contest not in user_stats[username]:
        user_stats[username][contest] = points
    else:
        user_stats[username][contest] = max(user_stats[username][contest], points)

for contest, user_data in contests_users.items():
    print(f"{contest}: {len(user_data)} participants")
    user_data_sorted = dict(sorted(user_data.items(), key=lambda x: (-x[1], x[0])))
    for i, (user, points) in enumerate(user_data_sorted.items(), 1):
        print(f"{i}. {user} <::> {points}")

print("Individual standings:")
individual_stats = {user: sum(points.values()) for user, points in user_stats.items()}
individual_stats_sorted = dict(sorted(individual_stats.items(), key=lambda x: (-x[1], x[0])))
for i, (user, points) in enumerate(individual_stats_sorted.items(), 1):
    print(f"{i}. {user} -> {points}")
