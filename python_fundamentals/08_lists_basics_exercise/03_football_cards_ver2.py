# https://judge.softuni.org/Contests/Compete/Index/1725#2

team_a = [str(i) for i in range(1, 12)]
team_b = [str(i) for i in range(1, 12)]

sequence_of_cards = list(input().split())
is_game_terminated = False
for el in sequence_of_cards:
    current_team, current_player = el.split("-")
    if current_team == "A":
        team_a.pop(team_a.index(current_player)) if current_player in team_a else None
    elif current_team == "B":
        team_b.pop(team_b.index(current_player)) if current_player in team_b else None

    if len(team_a) < 7 or len(team_b) < 7:
        is_game_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
print("Game was terminated") if is_game_terminated else None
