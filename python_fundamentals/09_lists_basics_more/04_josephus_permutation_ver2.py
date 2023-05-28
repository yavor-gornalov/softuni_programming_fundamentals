# https://judge.softuni.org/Contests/Practice/Index/1726#3

from collections import deque

people_circle = deque(input().split())
number_k = int(input())

execution_sequence = []
while people_circle:
    people_circle.rotate(-(number_k - 1))
    execution_sequence.append(people_circle.popleft())

print(f"[{','.join(execution_sequence)}]")
