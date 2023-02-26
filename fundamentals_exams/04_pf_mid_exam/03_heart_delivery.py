# https://judge.softuni.org/Contests/Practice/Index/2031#2

neighbourhood = [int(x) for x in input().split("@")]

house_idx = 0
while True:
    command = input()
    if command == "Love!":
        break
    command_args = command.split()
    action, length = command_args[0], int(command_args[1])
    if action == "Jump":
        house_idx += length
        if house_idx >= len(neighbourhood):
            house_idx = 0
        if neighbourhood[house_idx] == 0:
            print(f"Place {house_idx} already had Valentine's day.")
        else:
            neighbourhood[house_idx] -= 2
            if neighbourhood[house_idx] == 0:
                print(f"Place {house_idx} has Valentine's day.")

print(f"Cupid's last position was {house_idx}.")
if neighbourhood.count(0) == len(neighbourhood):
    print("Mission was successful.")
else:
    failed_house_count = len(neighbourhood) - neighbourhood.count(0)
    print(f"Cupid has failed {failed_house_count} places.")
