# https://judge.softuni.org/Contests/Practice/Index/1738#0

def read_contests():
    contests = set()
    while True:
        line = input()
        if line == "end of contests":
            break
        contest_name, contest_pass = line.split(":")
        contests.add((contest_name, contest_pass))
    return contests


def validate_contest(current_contest, current_pass, contests):
    return (current_contest, current_pass) in contests


def save_user_results(current_user, current_contest, current_points, user_submissions):
    if current_user not in user_submissions:
        user_submissions[current_user] = {current_contest: current_points}
    elif current_contest in user_submissions[current_user]:
        user_submissions[current_user][current_contest] = \
            max(user_submissions[current_user][current_contest], current_points)
    else:
        user_submissions[current_user][current_contest] = current_points


def get_best_candidate(user_submissions):
    best_candidate_name = ""
    best_candidate_result = 0
    for candidate, contests in user_submissions.items():
        candidate_result = sum(contests.values())
        if candidate_result > best_candidate_result:
            best_candidate_name = candidate
            best_candidate_result = candidate_result

    return best_candidate_name, best_candidate_result


all_contests = read_contests()
user_submissions = {}

while True:
    line = input()
    if line == "end of submissions":
        break
    contest, password, username, points = line.split("=>")

    if not validate_contest(contest, password, all_contests):
        continue

    save_user_results(username, contest, int(points), user_submissions)

user, result = get_best_candidate(user_submissions)

print(f"Best candidate is {user} with total {result} points.")
print("Ranking:")
for user, user_contests in sorted(user_submissions.items()):
    print(user)
    [print(f"#  {contest} -> {points}") for contest, points in sorted(user_contests.items(), key=lambda x: -x[1])]
