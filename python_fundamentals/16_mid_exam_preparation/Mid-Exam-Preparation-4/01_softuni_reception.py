# https://judge.softuni.org/Contests/Practice/Index/2474#0

employees_productivity = [int(input()) for _ in range(3)]
students_waiting = int(input())

total_productivity = sum(employees_productivity)

current_hour = 0
while students_waiting > 0:
    current_hour += 1
    if current_hour % 4 == 0:
        continue
    students_waiting -= total_productivity

print(f"Time needed: {current_hour}h.")
