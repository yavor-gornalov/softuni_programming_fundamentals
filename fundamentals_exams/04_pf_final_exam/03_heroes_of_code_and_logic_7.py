# https://judge.softuni.org/Contests/Practice/Index/2303#2

MAX_HEALTH = 100
MAX_MANA = 200
heroes = {}

n = int(input())
for _ in range(n):
    name, health, mana = input().split()
    heroes[name] = {
        "health": int(health),
        "mana": int(mana)
    }

while True:
    command = input()
    if command == "End":
        break
    command_args = command.split(" - ")
    action = command_args[0]
    hero = command_args[1]

    if action == "CastSpell":
        mp_needed = int(command_args[2])
        spell = command_args[3]
        if mp_needed > heroes[hero]["mana"]:
            print(f"{hero} does not have enough MP to cast {spell}!")
        else:
            heroes[hero]["mana"] -= mp_needed
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['mana']} MP!")
    elif action == "TakeDamage":
        damage = int(command_args[2])
        attacker = command_args[3]
        heroes[hero]["health"] = max(0, heroes[hero]["health"] - damage)
        if heroes[hero]["health"]:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['health']} HP left!")
        else:
            del heroes[hero]
            print(f"{hero} has been killed by {attacker}!")
    elif action == "Recharge":
        amount = int(command_args[2])
        if heroes[hero]["mana"] + amount > MAX_MANA:
            amount = MAX_MANA - heroes[hero]["mana"]
        heroes[hero]["mana"] += amount
        print(f"{hero} recharged for {amount} MP!")
    elif action == "Heal":
        amount = int(command_args[2])
        if heroes[hero]["health"] + amount > MAX_HEALTH:
            amount = MAX_HEALTH - heroes[hero]["health"]
        heroes[hero]["health"] += amount
        print(f"{hero} healed for {amount} HP!")

if heroes:
    for hero, hero_data in heroes.items():
        print(f"{hero}\n  HP: {hero_data['health']}\n  MP: {hero_data['mana']}")
