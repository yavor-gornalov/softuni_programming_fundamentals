# https://judge.softuni.org/Contests/Practice/Index/2303#2


def pick_heroes(heroes_count):
    heroes_dict = {}
    for _ in range(heroes_count):
        hero_name, hit_points, mana_points = input().split()
        heroes_dict[hero_name] = {"HP": int(hit_points), "MP": int(mana_points)}
    return heroes_dict


def cast_spell(hero, mp_needed_str, spell_name):
    mp_needed = int(mp_needed_str)
    if heroes[hero]["MP"] >= mp_needed:
        heroes[hero]["MP"] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['MP']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")


def take_damage(hero, damage_str, attacker):
    damage = int(damage_str)
    heroes[hero]["HP"] -= damage
    if heroes[hero]["HP"] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")
    else:
        del heroes[hero]
        print(f"{hero} has been killed by {attacker}!")


def recharge(hero, amount_str):
    amount = int(amount_str)
    current_mana = heroes[hero]["MP"]
    if current_mana + amount > MAX_MANA:
        amount = MAX_MANA - current_mana
    heroes[hero]["MP"] += amount
    print(f"{hero} recharged for {amount} MP!")


def heal(hero, amount_str):
    amount = int(amount_str)
    current_health = heroes[hero]["HP"]
    if current_health + amount > MAX_HIT:
        amount = MAX_HIT - current_health
    heroes[hero]["HP"] += amount
    print(f"{hero} healed for {amount} HP!")


commands = {
    "CastSpell": cast_spell,
    "TakeDamage": take_damage,
    "Recharge": recharge,
    "Heal": heal
}

MAX_HIT, MAX_MANA = 100, 200

number_of_heroes = int(input())
heroes = pick_heroes(number_of_heroes)

while True:
    line = input()
    if line == "End":
        break

    command, *args = line.split(" - ")
    commands[command](*args)

for hero, stats in heroes.items():
    print(f"{hero}\n"
          f"  HP: {stats['HP']}\n"
          f"  MP: {stats['MP']}")
