# https://judge.softuni.org/Contests/Practice/Index/2302#2

cities = {}

while True:
    command = input()
    if command == "Sail":
        break
    command_args = command.split("||")
    city = command_args[0]
    population = int(command_args[1])
    gold = int(command_args[2])
    if city not in cities:
        cities[city] = dict.fromkeys(["population", "gold"], 0)
    cities[city]["population"] += population
    cities[city]["gold"] += gold

while True:
    action = input()
    if action == "End":
        break
    action_args = action.split("=>")
    action = action_args[0]
    if action == "Plunder":
        town = action_args[1]
        people = int(action_args[2])
        gold = int(action_args[3])
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]["population"] <= 0 or cities[town]["gold"] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        town = action_args[1]
        gold = int(action_args[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, data in cities.items():
        print(f"{town} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
