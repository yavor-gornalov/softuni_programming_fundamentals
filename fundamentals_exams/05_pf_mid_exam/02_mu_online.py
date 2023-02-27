# https://judge.softuni.org/Contests/Practice/Index/2028#1

INITIAL_HEALTH, INITIAL_BITCOINS = 100, 0

dungeons_rooms = list(x for x in input().split("|"))
health, bitcoins = INITIAL_HEALTH, INITIAL_BITCOINS
alive = True
for room in dungeons_rooms:
    arguments = room.split()
    command, number = arguments[0], int(arguments[1])
    if command == "potion":
        amount = number if health + number <= 100 else INITIAL_HEALTH - health
        health = min(INITIAL_HEALTH, health + number)
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        monster, attack = command, number
        health -= attack
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.\n"
                  f"Best room: {dungeons_rooms.index(room) + 1}")
            alive = False
            break
else:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoins}\n"
          f"Health: {health}")
