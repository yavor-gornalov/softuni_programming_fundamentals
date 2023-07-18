# https://judge.softuni.org/Contests/Compete/Index/1737#4

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}
key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
junk_items = {

}

legendary_item_built = False
while not legendary_item_built:
    materials = input().lower().split()

    for idx in range(1, len(materials) + 1, 2):
        current_material = materials[idx]
        current_quantity = int(materials[idx - 1])

        if current_material in key_materials:
            key_materials[current_material] += current_quantity
            if key_materials[current_material] >= 250:
                key_materials[current_material] -= 250
                print(f"{legendary_items[current_material]} obtained!")
                legendary_item_built = True
                break
        elif current_material not in junk_items:
            junk_items[current_material] = current_quantity
        else:
            junk_items[current_material] += current_quantity

[print(f"{el}: {count}") for el, count in key_materials.items()]
[print(f"{el}: {count}") for el, count in junk_items.items()]
