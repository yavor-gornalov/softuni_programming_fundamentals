# https://judge.softuni.org/Contests/Practice/Index/1744#3

import re

health_pattern = r"[^0-9\.\+\-\*\/]"
health_redex = re.compile(health_pattern)

damage_pattern = r"(?P<damage>[\-|+]?[\d]+\.?[\d]*)"
damage_redex = re.compile(damage_pattern)

demon_names = [name.strip(' ') for name in input().split(',') if name]
demons = dict.fromkeys([name for name in demon_names if not name.isnumeric()])

for demon in demons:
    health_points = health_redex.findall(demon)
    health = sum([ord(ch) for ch in health_points])
    damage_points = damage_redex.finditer(demon)
    damage = sum([float(pts.group("damage")) for pts in damage_points])
    mul_count = demon.count("*")
    dev_count = demon.count("/")
    for _ in range(mul_count):
        damage *= 2
    for _ in range(dev_count):
        damage /= 2

    demons[demon] = {"health": health,
                     "damage": damage}

for demon, skills in sorted(demons.items(), key=lambda x: x):
    print(f"{demon} - {skills['health']} health, {skills['damage']:.2f} damage")
