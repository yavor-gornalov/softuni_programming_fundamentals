# https://judge.softuni.org/Contests/Practice/Index/2028#0

from math import ceil

students_count = int(input())
course_lectures = int(input())
additional_bonus = int(input())

student_attendances = [int(input()) for _ in range(students_count)]
max_attendances = max(student_attendances) if student_attendances else 0
max_bonus = ceil(max_attendances / course_lectures * (5 + additional_bonus)) if course_lectures else 0

print(f"Max Bonus: {max_bonus}.\n"
      f"The student has attended {max_attendances} lectures.")
