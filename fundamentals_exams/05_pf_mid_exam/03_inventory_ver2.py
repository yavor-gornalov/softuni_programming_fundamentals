# https://judge.softuni.org/Contests/Practice/Index/2028#2

def collect_item(arr, itm):
    if itm not in arr:
        arr.append(itm)
    return arr


def drop_item(arr, itm):
    if itm in arr:
        arr.remove(itm)
    return arr


def combine_items(arr, old_itm, new_itm):
    if old_itm in arr:
        arr.insert(arr.index(old_itm) + 1, new_itm)
    return arr


def renew_item(arr, itm):
    if itm in arr:
        itm_idx = arr.index(itm)
        arr.append(arr.pop(itm_idx))
    return arr


items = input().split(", ")

command = input()
while command != "Craft!":
    action, *tokens = command.split(" - ")

    if action == "Collect":
        item = tokens[0]
        items = collect_item(items, item)
    elif action == "Drop":
        item = tokens[0]
        items = drop_item(items, item)
    elif action == "Combine Items":
        old_item, new_item = tokens[0].split(":")
        items = combine_items(items, old_item, new_item)
    elif action == "Renew":
        item = tokens[0]
        items = renew_item(items, item)
    command = input()
print(*items, sep=", ")
