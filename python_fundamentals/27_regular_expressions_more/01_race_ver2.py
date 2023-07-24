# https://judge.softuni.org/Contests/Practice/Index/1744#0
import re


def get_player_name(text):
    return "".join(ch for ch in re.findall(r"[A-Za-z]", text))


def get_player_distance(text):
    return sum([int(d) for d in re.findall(r"\d", text)])


players = input().split(", ")
players_distances = dict.fromkeys(players, 0)
while True:
    line = input()
    if line == "end of race":
        break
    name = get_player_name(line)
    distance = get_player_distance(line)
    if name in players:
        players_distances[name] += distance

for i, (player, distance) in enumerate(sorted(players_distances.items(), key=lambda x: -x[1]), 1):
    if i == 1: print(f"1st place: {player}")
    if i == 2: print(f"2nd place: {player}")
    if i == 3: print(f"3rd place: {player}")
