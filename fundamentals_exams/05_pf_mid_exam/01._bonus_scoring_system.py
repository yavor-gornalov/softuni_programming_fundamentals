# https://judge.softuni.org/Contests/Practice/Index/2028#0

from math import ceil

students_count = int(input())  # [0…50]
lectures_count = int(input())  # [0…50]
additional_bonus = int(input())  # [0…100]

attendances = []
for _ in range(students_count):
    attendance = int(input())
    attendances.append(attendance)

max_attendances = max(attendances) if attendances else 0
total_bonus = max_attendances / lectures_count * (5 + additional_bonus) if lectures_count else 0

print(f"Max Bonus: {ceil(total_bonus)}.\nThe student has attended {max_attendances} lectures.")
