# https://judge.softuni.org/Contests/Compete/Index/1731#4

number_of_rooms = int(input())

total_free_chairs = 0
chairs_enoug = True
for room in range(1, number_of_rooms + 1):
    line = input().split()
    number_of_chairs, visitors = len(line[0]), int(line[1])
    if number_of_chairs < visitors:
        chairs_enoug = False
        print(f"{visitors - number_of_chairs} more chairs needed in room {room}")
    else:
        total_free_chairs += number_of_chairs - visitors
if chairs_enoug:
    print(f"Game On, {total_free_chairs} free chairs left")
