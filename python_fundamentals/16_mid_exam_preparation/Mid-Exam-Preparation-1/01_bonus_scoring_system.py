# https://judge.softuni.org/Contests/Practice/Index/2028#0

from math import ceil

students_count = int(input())  # [0:50]
lectures_count = int(input())  # [0:50]
additional_bonus = int(input())  # [0:100]

max_attendances = 0
for _ in range(students_count):
    attendances = int(input())
    max_attendances = max(attendances, max_attendances)

max_bonus = max_attendances / lectures_count * (5 + additional_bonus) if lectures_count else 0

print(f"Max Bonus: {ceil(max_bonus)}.\n"
      f"The student has attended {max_attendances} lectures.")
