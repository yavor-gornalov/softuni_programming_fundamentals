# https://judge.softuni.org/Contests/Practice/Index/1736#5

courses = input().lower().split()
course_dict = dict.fromkeys(courses, 0)
for course in courses:
    course_dict[course] += 1
[print(key, end=" ") for (key, count) in course_dict.items() if count % 2]
