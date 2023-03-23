# https://judge.softuni.org/Contests/Practice/Index/1744#2

import re

key_pattern = r"s|t|a|r"
key_regex = re.compile(key_pattern, re.IGNORECASE)

pattern = r"([^\@\-\,\!\,\:\>]*)@(?P<planet>[a-zA-Z]+)" \
          r"([^\@\-\,\!\,\:\>]*):(?P<population>\d+)" \
          r"([^\@\-\,\!\,\:\>]*)(!(?P<attack_type>[A|D])!)" \
          r"([^\@\-\,\!\,\:\>]*)\->(?P<soldiers_count>\d+)([^\@\-\,\!\,\:\>]*)"
regex = re.compile(pattern)

enigma = {}

n = int(input())
for _ in range(n):
    line = input()
    count = len(key_regex.findall(line))
    decrypted_message = "".join([chr(ord(ch) - count) for ch in line])
    try:
        planet = regex.match(decrypted_message).group("planet")
        population = regex.match(decrypted_message).group("population")
        attack_type = regex.match(decrypted_message).group("attack_type")
        soldiers_count = regex.match(decrypted_message).group("soldiers_count")
    except AttributeError:
        continue
    enigma[planet] = population, attack_type, soldiers_count

attached_planets = {k: val[0] for k, val in enigma.items() if val[1] == "A"}
destroyed_planets = {k: val[0] for k, val in enigma.items() if val[1] == "D"}

print(f"Attacked planets: {len(attached_planets)}")
for planet in sorted(attached_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
