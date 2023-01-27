# https://judge.softuni.org/Contests/Compete/Index/1719#7

total_coffees = 0
event_list = ['coding', "cat", 'dog', 'movie']
command = input()
while not command == "END":
    for event in event_list:
        if command == event.lower():
            total_coffees += 1
        elif command == event.upper():
            total_coffees += 2

    command = input()

if total_coffees > 5:
    print("You need extra sleep")
else:
    print(total_coffees)
