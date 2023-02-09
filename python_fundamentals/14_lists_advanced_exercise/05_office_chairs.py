# https://judge.softuni.org/Contests/Compete/Index/1731#4

number_of_rooms = int(input())

total_free_chairs = 0
missing_chairs = False
for room in range(1, number_of_rooms + 1):
    current_free_chairs = 0
    tokens = input().split()
    chairs = tokens[0].count("X")
    visitors = int(tokens[1])
    if chairs < visitors:
        missing_chairs = True
        print(f"{visitors - chairs} more chairs needed in room {room}")
    else:
        total_free_chairs += (chairs - visitors)
if not missing_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
