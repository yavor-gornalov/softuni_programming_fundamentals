# # https://judge.softuni.org/Contests/Practice/Index/1773#1

def loot(arr, items):
    for item in items:
        if item not in arr:
            arr.insert(0, item)
    return arr


def drop(arr, idx):
    if 0 <= idx < len(arr):
        arr.append(arr.pop(idx))
    return arr


def steal(arr, cnt):
    stolen_items = []
    for _ in range(cnt):
        if not arr:
            break
        stolen_items.insert(0, arr.pop())
    print(*stolen_items, sep=", ")
    return arr


actions = {
    "Loot": loot,
    "Drop": drop,
    "Steal": steal,
}

treasure_items = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break
    action, *tokens = command.split()
    if action in ["Drop", "Steal"]:
        tokens = int(tokens[0])

    treasure_items = actions[action](treasure_items, tokens)

if treasure_items:
    average_gain = sum([len(x) for x in treasure_items]) / len(treasure_items)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
