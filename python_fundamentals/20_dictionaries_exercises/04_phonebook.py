# https://judge.softuni.org/Contests/Practice/Index/1737#3

phonebook = {}

while True:
    command = input()
    if "-" not in command:
        n = int(command)
        break
    name, phone = command.split("-")
    phonebook[name] = phone

for _ in range(n):
    contact = input()
    if contact in phonebook:
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
