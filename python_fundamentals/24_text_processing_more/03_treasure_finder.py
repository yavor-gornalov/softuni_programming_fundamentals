# https://judge.softuni.org/Contests/Practice/Index/1741#2

key = [int(x) for x in input().split()]

while True:
    line = input()
    if line == "find":
        break
    message = ""
    for i, ch in enumerate(line):
        idx = i % len(key)
        ch = chr(ord(ch) - key[idx])
        message += ch
    treasure_type = message[message.find("&") + 1:message.rfind("&")]
    treasure_coordinates = message[message.find("<") + 1:message.find(">")]
    print(f"Found {treasure_type} at {treasure_coordinates}")
