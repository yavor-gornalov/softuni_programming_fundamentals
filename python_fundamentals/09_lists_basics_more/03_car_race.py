# https://judge.softuni.org/Contests/Practice/Index/1726#2

race_sequence = list(map(int, input().split()))

left_racer_time = 0
right_racer_time = 0
left_start = 0
right_start = len(race_sequence) - 1
finish = len(race_sequence) // 2

for i in range(left_start, finish):
    current_time = race_sequence[i]
    left_racer_time += current_time
    if current_time == 0:
        left_racer_time *= 0.8

for j in range(right_start, finish, -1):
    current_time = race_sequence[j]
    right_racer_time += current_time
    if current_time == 0:
        right_racer_time *= 0.8

if left_racer_time <= right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
