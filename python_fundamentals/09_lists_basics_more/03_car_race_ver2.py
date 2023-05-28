# https://judge.softuni.org/Contests/Practice/Index/1726#2

from collections import deque

race_stages = deque([int(x) for x in input().split()])

car_times = [0, 0]
while len(race_stages) > 1:
    current_times = [race_stages.popleft(), race_stages.pop()]
    for i in range(2):
        if current_times[i] != 0:
            car_times[i] += current_times[i]
        else:
            car_times[i] = 0.8 * car_times[i]

if car_times[0] <= car_times[1]:
    print(f"The winner is left with total time: {car_times[0]:.1f}")
else:
    print(f"The winner is right with total time: {car_times[1]:.1f}")
