# https://judge.softuni.org/Contests/Practice/Index/1726#3

person_list = list(map(int, input().split()))
k_person = int(input())
executed_list = []

counter = 0
index = 0
while person_list:
    counter += 1
    if counter % k_person == 0:
        executed_list.append(person_list.pop(index))
    else:
        index += 1

    if index >= len(person_list):
        index = 0

print(str(executed_list).replace(" ", ""))
