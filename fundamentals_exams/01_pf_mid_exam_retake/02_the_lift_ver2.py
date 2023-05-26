# https://judge.softuni.org/Contests/Practice/Index/2517#1

MAX_CAPACITY = 4

people_waiting = int(input())
lift = [int(x) for x in input().split()]

for idx in range(len(lift)):
    if people_waiting == 0:
        break
    elif people_waiting + lift[idx] < MAX_CAPACITY:
        lift[idx] += people_waiting
        people_waiting = 0
        break
    people_waiting -= MAX_CAPACITY - lift[idx]
    lift[idx] = MAX_CAPACITY

if not all(wagon == MAX_CAPACITY for wagon in lift):
    print("The lift has empty spots!")
elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
print(*lift, sep=" ")
