# https://judge.softuni.org/Contests/Practice/Index/2518#2

def gather_plants(count):
    plants_dict = {}
    for _ in range(count):
        plant, rarity = input().split("<->")
        plants_dict[plant] = [int(rarity), []]
    return plants_dict


def show_exhibition_results(plants_dict):
    print(f"Plants for the exhibition:")
    for plant, (rarity, ratings) in plants_dict.items():
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        print(f"- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}")


def plant_exists(plant):
    return plant in plants


def rate_plant(plant, rating_str, plants_dict):
    plants_dict[plant][1].append(float(rating_str))
    return plants_dict


def update_plant(plant, new_rarity_str, plants_dict):
    plants_dict[plant][0] = int(new_rarity_str)
    return plants_dict


def reset_plant(plant, plants_dict):
    plants_dict[plant][1].clear()
    return plants_dict


commands = {
    "Rate": rate_plant,
    "Update": update_plant,
    "Reset": reset_plant
}

plants_count = int(input())
plants = gather_plants(plants_count)

while True:
    line = input()
    if line == "Exhibition":
        show_exhibition_results(plants)
        break

    command, args_str = line.split(": ")
    current_plant, *args = args_str.split(" - ")

    if not plant_exists(current_plant):
        print("error")
        continue

    plants = commands[command](current_plant, *args, plants)
