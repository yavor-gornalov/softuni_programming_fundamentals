# https://judge.softuni.org/Contests/Compete/Index/1737#6

def register_user(user, license_plate):
    message = ""
    if user not in parking_lot:
        parking_lot[user] = license_plate
        message = f"{user} registered {license_plate} successfully"
    elif parking_lot[user] == license_plate:
        message = f"ERROR: already registered with plate number {license_plate}"
    return message


def unregister_user(user):
    message = ""
    if user not in parking_lot:
        message = f"ERROR: user {user} not found"
    else:
        del parking_lot[user]
        message = f"{user} unregistered successfully"
    return message


commands = {
    "register": register_user,
    "unregister": unregister_user
}

parking_lot = {}

for _ in range(int(input())):
    command, *args = input().split()
    print(commands[command](*args))

[print(f"{usr} => {plate}") for usr, plate in parking_lot.items()]
