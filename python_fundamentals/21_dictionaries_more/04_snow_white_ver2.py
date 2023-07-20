# https://judge.softuni.org/Contests/Practice/Index/1738#3

def add_dwarf(name, hat_color, physics):
    if (name, hat_color) not in dwarfs:
        dwarfs[(name, hat_color)] = [int(physics)]
    dwarfs[(name, hat_color)][0] = max(dwarfs[(name, hat_color)][0], int(physics))


dwarfs = {}
command = input()
while command != "Once upon a time":
    args = command.split(" <:> ")
    add_dwarf(*args)
    command = input()

for (name, color), data in dwarfs.items():
    data.append(len([x for x in dwarfs if color == x[1]]))

for (name, hat_color), (physics, count) in sorted(dwarfs.items(), key=lambda x: (-x[1][0], -x[1][1])):
    print(f"({hat_color}) {name} <-> {physics}")
