# https://judge.softuni.org/Contests/Compete/Index/1737#9

companies = {}

line = input()
while line != "End":
    company_name, employee_id = line.split(" -> ")

    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

    line = input()

for company, employees in companies.items():
    print(company)
    [print(f"-- {employee_id}") for employee_id in employees]
