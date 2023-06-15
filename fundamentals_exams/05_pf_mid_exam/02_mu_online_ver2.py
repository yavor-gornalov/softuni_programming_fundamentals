# https://judge.softuni.org/Contests/Practice/Index/2028#1

initial_health, initial_bitcoins = 100, 0

dungeons_rooms = input().split("|")

current_health, current_bitcoins = initial_health, initial_bitcoins

room_number = 0
for room in dungeons_rooms:
    command, number = room.split()[0], int(room.split()[1])
    room_number += 1

    if command == "potion":
        if current_health + number < initial_health:
            amount = number
        else:
            amount = initial_health - current_health
        current_health += amount
        print(f"You healed for {amount} hp.\n"
              f"Current health: {current_health} hp.")

    elif command == "chest":
        current_bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        current_health -= number
        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.\n"
                  f"Best room: {room_number}")
            break
else:
    print(f"You've made it!\n"
          f"Bitcoins: {current_bitcoins}\n"
          f"Health: {current_health}")
