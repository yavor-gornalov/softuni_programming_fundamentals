# https://judge.softuni.org/Contests/Compete/Index/1737#10

def get_user_side(user):
    for side, users in force_sides.items():
        if user in users:
            return side
    return None


def add_force_user(side, user):
    if user in force_users:
        return

    if side not in force_sides:
        force_sides[side] = [user]
    else:
        force_sides[side].append(user)
    force_users.add(user)


def change_user_side(user, new_side):
    if user in force_users:
        user_side = get_user_side(user)
        force_sides[user_side].remove(user)
        force_users.remove(user)

    if new_side not in force_sides:
        force_sides[new_side] = [user]
    else:
        force_sides[new_side].append(user)
    force_users.add(user)

    print(f"{user} joins the {new_side} side!")


commands = {
    " | ": add_force_user,
    " -> ": change_user_side
}

force_sides = {}
force_users = set()

while True:
    line = input()
    if line == "Lumpawaroo":
        break
    for command in commands:
        if command in line:
            args = line.split(command)
            commands[command](*args)
            continue

for side, users in force_sides.items():
    if not users:
        continue
    print(f"Side: {side}, Members: {len(users)}")
    [print(f"! {user}") for user in users]
