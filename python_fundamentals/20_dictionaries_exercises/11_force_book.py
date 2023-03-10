# https://judge.softuni.org/Contests/Practice/Index/1737#10

def is_user_exists(seq, usr):
    for usr_lst in seq.values():
        if usr in usr_lst:
            return True
    return False


def get_user_side(seq, usr):
    for usr_side, usr_list in seq.items():
        if usr in usr_list:
            return usr_side
    return None


force_book = {}
user_exists = False
while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        side, user = command.split(" | ")

        if is_user_exists(seq=force_book, usr=user):
            continue

        if not force_book.get(side):
            force_book[side] = []
        force_book[side].append(user)

    elif " -> " in command:
        user, new_side = command.split(" -> ")
        user_side = get_user_side(seq=force_book, usr=user)

        if not force_book.get(new_side):
            force_book[new_side] = []

        if user_side:
            force_book[user_side].remove(user)
        force_book[new_side].append(user)

        print(f"{user} joins the {new_side} side!")

for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        [print(f"! {user}") for user in force_book[side]]
