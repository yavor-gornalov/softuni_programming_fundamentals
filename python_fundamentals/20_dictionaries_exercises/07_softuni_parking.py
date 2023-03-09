# https://judge.softuni.org/Contests/Practice/Index/1737#6

parking = {}

n = int(input())

for _ in range(n):
    command = input().split()
    action, username = command[0], command[1]
    if action == "register":
        license_plate = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
            continue
        parking[username] = license_plate
        print(f"{username} registered {license_plate} successfully")
    elif action == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
            continue
        del parking[username]
        print(f"{username} unregistered successfully")

[print(f"{username} => {parking[username]}") for username in parking]
