# https://judge.softuni.org/Contests/Practice/Index/1738#1


def save_submission(user, contest, user_points, submissions):
    points = int(user_points)
    if user not in submissions:
        submissions[user] = {contest: points}
    elif contest not in submissions[user]:
        submissions[user][contest] = points
    else:
        submissions[user][contest] = max(submissions[user][contest], points)


def save_contest(user, contest, user_points, contests):
    points = int(user_points)
    if contest not in contests:
        contests[contest] = {user: points}
    elif user not in contests[contest]:
        contests[contest][user] = points
    else:
        contests[contest][user] = max(contests[contest][user], points)


all_contests = {}
user_submissions = {}

while True:
    command = input()
    if command == "no more time":
        break

    args = command.split(" -> ")

    save_submission(*args, user_submissions)
    save_contest(*args, all_contests)

for contest, user_results in all_contests.items():
    print(f"{contest}: {len(user_results)} participants")
    for i, (user, result) in enumerate(sorted(user_results.items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{i}. {user} <::> {result}")

print("Individual standings:")
for i, (user, results) in enumerate(sorted(user_submissions.items(), key=lambda x: (-sum(x[1].values()), x[0])), 1):
    print(f"{i}. {user} -> {sum(results.values())}")
