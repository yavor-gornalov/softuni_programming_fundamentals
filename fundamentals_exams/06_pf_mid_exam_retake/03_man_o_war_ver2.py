# https://judge.softuni.org/Contests/Practice/Index/1773#2

def invalid_index(idx, ship):
    return not 0 <= idx < len(ship)


def ship_status(ship):
    return len([s for s in ship if s < max_section_health / 5])


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_section_health = int(input())

stalemate = True
while True:
    line = input()
    if line == "Retire":
        break
    command, *tokens = line.split()

    if command == "Fire":
        index, damage = [int(x) for x in tokens]
        if invalid_index(index, warship):
            continue
        if warship[index] <= damage:
            stalemate = False
            print("You won! The enemy ship has sunken.")
            break
        warship[index] -= damage
    elif command == "Defend":
        start_index, end_index, damage = [int(x) for x in tokens]
        if invalid_index(start_index, pirate_ship) or invalid_index(end_index, pirate_ship):
            continue
        if any(s < damage for s in pirate_ship[start_index:end_index + 1]):
            stalemate = False
            print("You lost! The pirate ship has sunken.")
            break
        for i in range(start_index, end_index + 1):
            pirate_ship[i] -= damage
    elif command == "Repair":
        index, health = [int(x) for x in tokens]
        if invalid_index(index, pirate_ship):
            continue
        pirate_ship[index] = min(pirate_ship[index] + health, max_section_health)
    elif command == "Status":
        print(f"{ship_status(pirate_ship)} sections need repair.")

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}\n"
          f"Warship status: {sum(warship)}")
