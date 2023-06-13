# https://judge.softuni.org/Contests/Practice/Index/1773#1

treasure = [x for x in input().split("|")]

is_empty, command = False, input()
while not command == "Yohoho!":
    command_args = command.split()
    command = command_args.pop(0)
    if command == "Loot":
        items = [item for item in command_args if item not in treasure]
        [treasure.insert(0, x) for x in items]
    elif command == "Drop":
        index = int(command_args[0])
        if 0 <= index < len(treasure):
            treasure.append(treasure.pop(index))
    elif command == "Steal":
        count = int(command_args[0])
        if count >= len(treasure):
            is_empty = True
        stolen_items = treasure[-count:]
        print(', '.join(stolen_items))
        treasure = treasure[:-count]
    command = input()

if is_empty:
    print("Failed treasure hunt.")
else:
    average_gain = sum(len(item) for item in treasure) / len(treasure) if treasure else 0
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
