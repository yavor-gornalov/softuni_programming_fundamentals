# https://judge.softuni.org/Contests/Practice/Index/1730#6

employees = [int(x) for x in input().split(" ")]
happiness_factor = int(input())

employees = list(map(lambda employee: employee * happiness_factor, employees))
average_happiness = sum(employees) / len(employees)
happy_employees = list(filter(lambda x: x >= average_happiness, employees))
if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")
