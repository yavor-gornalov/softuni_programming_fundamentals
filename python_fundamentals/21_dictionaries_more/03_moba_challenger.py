# https://judge.softuni.org/Contests/Practice/Index/1738#2

def is_battle_possible(player1, player2):
    if player1 not in players_pool or player2 not in players_pool:
        return False
    battle_possible = False
    for p in players_pool[player1]:
        if p in players_pool[player2]:
            battle_possible = True
            break
    return battle_possible


def demoted_player(player1, player2):
    player1_total = sum(players_pool[player1].values())
    player2_total = sum(players_pool[player2].values())

    if player1_total > player2_total:
        return player2
    elif player2_total > player1_total:
        return player1
    return None


players_pool = {}

while True:
    command = input()
    if command == "Season end":
        break
    if " -> " in command:
        args = command.split(" -> ")
        player, position = args[0], args[1]
        skill = int(args[2])
        if player not in players_pool:
            players_pool[player] = {}
        if position not in players_pool[player]:
            players_pool[player][position] = skill
        players_pool[player][position] = max(players_pool[player][position], skill)

    elif " vs " in command:
        args = command.split(" vs ")
        first_player, second_player = args[0], args[1]
        if not is_battle_possible(first_player, second_player):
            continue
        looser = demoted_player(first_player, second_player)
        if looser:
            del players_pool[looser]

# sorting outer dict by sum of values and alphabetically
sorted_pool = dict(sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0])))
for player, player_data in sorted_pool.items():
    print(f"{player}: {sum(player_data.values())} skill")
    sorted_player_data = dict(sorted(player_data.items(), key=lambda x: (-x[1], x[0])))
    for pos, skl in sorted_player_data.items():
        print(f"- {pos} <::> {skl}")
