# TODO: https://judge.softuni.org/Contests/Compete/Index/1731#10
# TODO: check out code in Softuni Judge system


def add_lesson(seq, title): return seq.append(title) if title not in seq else seq


def remove_lesson(seq, title):
    return [seq.pop(seq.index(title)) if title in seq else seq for title in [title, f"Exercise:{title}"]]


def insert_lesson(seq, title, index): return seq.insert(index, title) if title not in seq else seq


def swap_lesson(seq, title_1, title_2):
    if title_1 and title_2 in seq:
        index_1 = seq.index(title_1)
        index_2 = seq.index(title_2)
        seq[index_1], seq[index_2] = seq[index_2], seq[index_1]
        if f"Exercise:{title_1}" and f"Exercise:{title_2}" in seq:
            index_1 += 1
            index_2 += 1
            seq[index_1], seq[index_2] = seq[index_2], seq[index_1]
        elif f"Exercise:{title_1}" in seq or f"Exercise:{title_2}" in seq:
            seq.insert(index_2 + 1, seq.pop(index_1 + 1))


def exercise(seq, title):
    if title in seq:
        index = seq.index(title)
        insert_lesson(seq, f"Exercise:{title}", index + 1)
    else:
        add_lesson(seq, title)
        add_lesson(seq, f"Exercise:{title}")


# main
course_database = [x for x in input().split(", ")]

command = input()
while not command == "course start":
    tokens = command.split(":")
    action = tokens[0]
    lesson = tokens[1]
    if action == "Add":
        add_lesson(seq=course_database, title=lesson)
    elif action == "Insert":
        number = int(tokens[2])
        insert_lesson(seq=course_database, title=lesson, index=number)
    elif action == "Remove":
        remove_lesson(seq=course_database, title=lesson)
    elif action == "Swap":
        lesson_2 = tokens[2]
        swap_lesson(seq=course_database, title_1=lesson, title_2=lesson_2)
    elif action == "Exercise":
        exercise(seq=course_database, title=lesson)

    command = input()

for i, course in enumerate(course_database):
    print(f"{i + 1}.{course}")
