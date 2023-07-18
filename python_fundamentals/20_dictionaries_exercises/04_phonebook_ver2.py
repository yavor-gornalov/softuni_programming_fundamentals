# https://judge.softuni.org/Contests/Compete/Index/1737#3

phonebook = {}

line = input()
while not line.isalnum():
    name, number = line.split("-")
    phonebook[name] = number
    line = input()

contacts_count = int(line)
for _ in range(contacts_count):
    searched_name = input()
    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
