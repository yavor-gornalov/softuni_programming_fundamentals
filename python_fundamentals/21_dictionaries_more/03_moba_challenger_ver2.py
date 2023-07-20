# https://judge.softuni.org/Contests/Practice/Index/1738#2

def add_player(player, position, skill):
    current_skill = int(skill)
    if player not in players:
        players[player] = {position: current_skill}
    elif position not in players[player]:
        players[player][position] = current_skill
    else:
        players[player][position] = max(players[player][position], current_skill)


def validate_players(*args):
    for player in args:
        if player not in players:
            return False
    return True


def get_common_positions(first_player, second_player):
    common_positions = set()
    for position in players[first_player]:
        if position in players[second_player]:
            common_positions.add(position)

    return common_positions


def battle(first_player, second_player):
    if not validate_players(first_player, second_player):
        return

    common_positions = get_common_positions(first_player, second_player)

    if not common_positions:
        return

    first_player_total = sum(players[first_player].values())
    second_player_total = sum(players[second_player].values())
    if first_player_total > second_player_total:
        del players[second_player]
    elif second_player_total > first_player_total:
        del players[first_player]


commands = {
    " -> ": add_player,
    " vs ": battle,
}

players = {}

while True:
    line = input()
    if line == "Season end":
        break
    for command in commands:
        if command in line:
            tokens = line.split(command)
            commands[command](*tokens)
            continue

for player, attributes in sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(attributes.values())} skill")
    for attribute, points in sorted(attributes.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {attribute} <::> {points}")
