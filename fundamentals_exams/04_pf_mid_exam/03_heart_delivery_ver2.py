# https://judge.softuni.org/Contests/Practice/Index/2031#2

neighborhood = [int(x) for x in input().split("@")]

house_index = 0
while True:
    line = input()
    if line == "Love!":
        break

    jump_length = int(line.split()[-1])
    if house_index + jump_length < len(neighborhood):
        house_index += jump_length
    else:
        house_index = 0

    if neighborhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
        continue
    elif neighborhood[house_index] == 2:
        print(f"Place {house_index} has Valentine's day.")

    neighborhood[house_index] -= 2

houses_missed_valentine = 0
for house in neighborhood:
    if house > 0:
        houses_missed_valentine += 1

print(f"Cupid's last position was {house_index}.")
if not houses_missed_valentine:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {houses_missed_valentine} places.")
