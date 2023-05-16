# https://judge.softuni.org/Contests/Compete/Index/1722#6

number = int(input())

tank_capacity = 255
free_capacity = tank_capacity
for i in range(number):
    if free_capacity <= 0:
        break
    current_litters = int(input())
    if current_litters > free_capacity:
        print("Insufficient capacity!")
        continue
    free_capacity -= current_litters

print(tank_capacity - free_capacity)
