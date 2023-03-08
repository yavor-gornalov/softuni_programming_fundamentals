# https://judge.softuni.org/Contests/Practice/Index/1737#4
# TODO: problem not finished
materials = dict.fromkeys(["shards", "fragments", "motes"], 0)

LIMIT, item_obtained = 250, False
while not item_obtained:
    sequence = input().split()
    for el in range(1, len(sequence), 2):
        max_value = max(materials.values())
        if max_value >= LIMIT:
            if max_value == materials["shards"]:
                materials["shards"] -= LIMIT
                print("Shadowmourne obtained!")
                item_obtained = True
                break
            elif max_value == materials["fragments"]:
                materials["fragments"] -= LIMIT
                print("Valanyr obtained!")
                item_obtained = True
                break
            elif max_value == materials["motes"]:
                materials["motes"] -= LIMIT
                print("Dragonwrath obtained!")
                item_obtained = True
                break
        key = sequence[el].lower()
        quantity = int(sequence[el - 1])
        if key not in materials:
            materials[key] = 0
        materials[key] += quantity

[print(f"{key}: {materials[key]}") for key in materials]
