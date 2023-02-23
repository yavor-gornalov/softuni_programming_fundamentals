# https://judge.softuni.org/Contests/Practice/Index/2474#0

number_of_employees = 3
employee_efficiency = []
for _ in range(number_of_employees):
    employee_efficiency.append(int(input()))
students_count = int(input())

student_served_per_hour = sum(employee_efficiency)

hour_counter = 0
while students_count > 0:
    hour_counter += 1
    if not hour_counter % 4:
        continue
    students_count -= student_served_per_hour

print(f"Time needed: {hour_counter}h.")
