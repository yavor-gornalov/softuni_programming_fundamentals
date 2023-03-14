# https://judge.softuni.org/Contests/Practice/Index/1738#3

dwarfs = {}

while True:
    line = input()
    if line == "Once upon a time":
        break
    args = line.split(" <:> ")
    dwarf_name, dwarf_color = args[0], args[1]
    dwarf_height = int(args[2])

    if dwarf_color not in dwarfs:
        dwarfs[dwarf_color] = {}
    if dwarf_name not in dwarfs[dwarf_color]:
        dwarfs[dwarf_color][dwarf_name] = dwarf_height
    else:
        dwarfs[dwarf_color][dwarf_name] = max(dwarfs[dwarf_color][dwarf_name], dwarf_height)

dwarfs_info = {f"{color}:{name}": (height, len(dwarf_data.items()))
               for color, dwarf_data in dwarfs.items()
               for name, height in dwarf_data.items()}

for dwarf, info in sorted(dwarfs_info.items(), key=lambda x: (-x[1][0], -x[1][1])):
    dwarf_args = dwarf.split(":")
    color, name = dwarf_args[0], dwarf_args[1]
    height = info[0]
    print(f"({color}) {name} <-> {height}")
