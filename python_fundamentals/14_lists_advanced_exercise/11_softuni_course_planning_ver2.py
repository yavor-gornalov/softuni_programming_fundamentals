# https://judge.softuni.org/Contests/Compete/Index/1731#10


def add_lesson(title):
    if title not in lessons:
        lessons.append(title)


def insert_lesson(title, idx):
    if title not in lessons:
        lessons.insert(int(idx), title)


def remove_lesson(title):
    if title in lessons:
        lessons.remove(title)
    if f"{title}-Exercise" in lessons:
        lessons.remove(f"{title}-Exercise")


def swap_lessons(first_title, second_title):
    if first_title in lessons and second_title in lessons:
        first_idx = lessons.index(first_title)
        second_idx = lessons.index(second_title)
        lessons[first_idx], lessons[second_idx] = lessons[second_idx], lessons[first_idx]
        if f"{first_title}-Exercise" in lessons:
            lessons.remove(f"{first_title}-Exercise")
            add_exercise(first_title)
        if f"{second_title}-Exercise" in lessons:
            lessons.remove(f"{second_title}-Exercise")
            add_exercise(second_title)


def add_exercise(title):
    if title in lessons:
        lesson_idx = lessons.index(title)
        insert_lesson(f"{title}-Exercise", lesson_idx + 1)
    else:
        add_lesson(title)
        add_lesson(f"{title}-Exercise")


commands = {
    "Add": add_lesson,
    "Insert": insert_lesson,
    "Remove": remove_lesson,
    "Swap": swap_lessons,
    "Exercise": add_exercise,
}

lessons = input().split(", ")

line = input()
while not line == "course start":
    key, *args = line.split(":")
    commands[key](*args)
    line = input()

[print(f"{i}.{t}") for i, t in enumerate(lessons, 1)]
