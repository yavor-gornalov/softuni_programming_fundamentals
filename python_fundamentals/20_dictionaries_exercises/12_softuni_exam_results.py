# https://judge.softuni.org/Contests/Practice/Index/1737#11

submission_list = {}
submission_counters = {}
banned_users_list = []
while True:
    command = input()
    if command == "exam finished":
        break

    command_args = command.split("-")
    username, language = command_args[0], command_args[1]
    if language == "banned":
        banned_users_list.append(username)
        continue

    points = int(command_args[2])

    if language not in submission_list:
        submission_list[language] = {}
        submission_counters[language] = 0
    submission_counters[language] += 1

    if username not in submission_list[language]:
        submission_list[language][username] = 0

    submission_list[language][username] = max(submission_list[language][username], points)

print("Results:")
for language_users in submission_list.values():
    for usr, pts in language_users.items():
        if usr not in banned_users_list:
            print(usr, pts, sep=" | ")

print("Submissions:")
for language in submission_list:
    print(language, submission_counters[language], sep=" - ")
