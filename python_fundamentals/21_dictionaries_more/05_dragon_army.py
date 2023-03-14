# https://judge.softuni.org/Contests/Practice/Index/1738#4

n = int(input())
defaults = {
    "damage": 45,
    "health": 250,
    "armor": 10
}
dragons = {}
for _ in range(n):
    color, name, damage, health, armor = input().split()
    damage = int(damage) if damage != "null" else defaults["damage"]
    health = int(health) if health != "null" else defaults["health"]
    armor = int(armor) if armor != "null" else defaults["armor"]
    if color not in dragons:
        dragons[color] = {}
    if name not in dragons:
        dragons[color][name] = tuple(defaults.values())
    dragons[color][name] = (health, damage, armor)

for color, dragon_data in dragons.items():
    dragon_data_sorted = dict(sorted(dragon_data.items(), key=lambda x: x[0]))
    damage_avg, health_avg, armor_avg = 0, 0, 0
    count = len(dragon_data)
    dragon_stats = []
    for name, skills in dragon_data_sorted.items():
        health, damage, armor = skills
        damage_avg += damage
        health_avg += health
        armor_avg += armor
        dragon_stats.append(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")

    damage_avg /= count if count > 0 else 0
    health_avg /= count if count > 0 else 0
    armor_avg /= count if count > 0 else 0
    print(f"{color}::({damage_avg:.2f}/{health_avg:.2f}/{armor_avg:.2f})")
    print("\n".join(dragon_stats))
