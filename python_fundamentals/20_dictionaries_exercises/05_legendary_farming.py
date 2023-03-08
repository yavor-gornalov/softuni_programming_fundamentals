# https://judge.softuni.org/Contests/Practice/Index/1737#4

specials = dict.fromkeys(["shards", "fragments", "motes"], 0)
junks = {}

LIMIT, is_crafted = 250, False
while not is_crafted:
    sequence = input().split()
    for el in range(1, len(sequence), 2):
        key = sequence[el].lower()
        quantity = int(sequence[el - 1])
        if key in specials:
            specials[key] += quantity
            if specials[key] >= LIMIT:
                specials[key] -= LIMIT
                if key == "shards":
                    print("Shadowmourne obtained!")
                elif key == "fragments":
                    print("Valanyr obtained!")
                elif key == "motes":
                    print("Dragonwrath obtained!")
                is_crafted = True
                break

        elif key not in junks:
            junks[key] = quantity
        else:
            junks[key] += quantity

[print(f"{key}: {specials[key]}") for key in specials]
[print(f"{key}: {junks[key]}") for key in junks]
