# https://judge.softuni.org/Contests/Practice/Index/1738#4

def add_stats(damage, health, armor):
    default_stats = {"health": 250, "damage": 45, "armor": 10}
    current_stats = {"health": health, "damage": damage, "armor": armor}
    for stat, value in current_stats.items():
        if value == "null":
            current_stats[stat] = default_stats[stat]
        else:
            current_stats[stat] = int(value)
    return current_stats


def add_dragon(color, dragon, damage, health, armor, dragon_dict):
    if color not in dragon_dict:
        dragon_dict[color] = {}
    if dragon not in dragon_dict[color]:
        dragon_dict[color][dragon] = {}
    dragon_dict[color][dragon] = add_stats(damage, health, armor)


def generate_dragons(count):
    dragon_dict = {}
    for _ in range(count):
        args = input().split()
        add_dragon(*args, dragon_dict)
    return dragon_dict


def print_dragons(dragon_dict):
    for color, dragons_group in dragon_dict.items():
        group_damage = group_health = group_armor = 0
        for stat in dragons_group.values():
            group_damage += stat["damage"]
            group_health += stat["health"]
            group_armor += stat["armor"]
        avg_damage = group_damage / len(dragons_group)
        avg_health = group_health / len(dragons_group)
        avg_armor = group_armor / len(dragons_group)
        print(f"{color}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
        for drag, stats in sorted(dragons_group.items()):
            print(f"-{drag} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")


number_of_dragons = int(input())

dragons = generate_dragons(number_of_dragons)
print_dragons(dragons)
