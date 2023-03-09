# https://judge.softuni.org/Contests/Practice/Index/1737#9

companies = {}

while True:
    command = input()
    if command == "End":
        break
    command_args = command.split(" -> ")
    company, employee_id = command_args[0], command_args[1]
    if company not in companies:
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company in companies:
    print(company)
    for employee in companies[company]:
        print(f"-- {employee}")
