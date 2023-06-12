# https://judge.softuni.org/Contests/Practice/Index/2517#1

waiting_people = int(input())
lift = [int(x) for x in input().split()]
wagon_capacity = 4

for idx, current_wagon in enumerate(lift):
    if current_wagon < wagon_capacity:
        free_space = wagon_capacity - current_wagon
        if free_space > waiting_people:
            lift[idx] += waiting_people
            waiting_people = 0
            print("The lift has empty spots!")
            break
        waiting_people -= free_space
        lift[idx] = wagon_capacity

if waiting_people:
    print(f"There isn't enough space! {waiting_people} people in a queue!")

print(*lift, sep=" ")
