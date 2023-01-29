# https://judge.softuni.org/Contests/Compete/Index/1725#2

team_a = list(range(1, 12))
team_b = list(range(1, 12))

game_terminated = False
card_string = input().split(" ")
for card in card_string:
    team, player = card.split("-")
    if team == "A":
        if int(player) in team_a:
            team_a.remove(int(player))
    elif team == "B":
        if int(player) in team_b:
            team_b.remove(int(player))
    if len(team_a) < 7 or len(team_b) < 7:
        game_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_terminated:
    print("Game was terminated")
