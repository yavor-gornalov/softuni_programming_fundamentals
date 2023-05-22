# https://judge.softuni.org/Contests/Compete/Index/1725#6

def out_of_stock(gift):
    while gift in gifts:
        gifts[gifts.index(gift)] = "None"


def required_gift(gift, index):
    if 0 <= int(index) < len(gifts):
        gifts[int(index)] = gift


def just_in_case(gift):
    gifts[-1] = gift if gifts else None


commands = {
    "OutOfStock": out_of_stock,
    "Required": required_gift,
    "JustInCase": just_in_case
}

gifts = input().split()

while True:
    line = input()
    if line == 'No Money':
        break
    command, *tokens = line.split()
    commands[command](*tokens)

print(*[gift for gift in gifts if gift != "None"], sep=" ")
