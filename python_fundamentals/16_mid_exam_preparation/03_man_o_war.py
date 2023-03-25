# https://judge.softuni.org/Contests/Practice/Index/1773#2

pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
max_health_capacity = int(input())

ship_destroyed = False
while not ship_destroyed:
    command = input()
    if command == "Retire":
        break

    arguments = command.split()
    command = arguments[0]
    if command == "Fire":
        index = int(arguments[1])
        if not 0 <= index < len(war_ship):
            continue
        damage = int(arguments[2])
        war_ship[index] -= damage
        if war_ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            ship_destroyed = True
    elif command == "Defend":
        start_index = int(arguments[1])
        end_index = int(arguments[2])
        if not 0 <= start_index < end_index < len(pirate_ship):
            continue
        damage = int(arguments[3])
        for index in range(start_index, end_index + 1):
            pirate_ship[index] -= damage
            if pirate_ship[index] <= 0:
                print("You lost! The pirate ship has sunken.")
                ship_destroyed = True
                break

    elif command == "Repair":
        index = int(arguments[1])
        if not 0 <= index < len(pirate_ship):
            continue
        health = int(arguments[2])
        pirate_ship[index] = min(max_health_capacity, pirate_ship[index] + health)

    elif command == "Status":
        low_capacity_limit = 0.20 * max_health_capacity
        sections_for_repair = sum([1 if x < low_capacity_limit else 0 for x in pirate_ship])
        print(f"{sections_for_repair} sections need repair.")

if not ship_destroyed:
    print(f"Pirate ship status: {sum(pirate_ship)}\n"
          f"Warship status: {sum(war_ship)}")
