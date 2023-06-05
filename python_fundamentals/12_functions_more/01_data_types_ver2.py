# https://judge.softuni.org/Contests/Practice/Index/1729#0

data_types = {
    "int": lambda x: 2 * int(x),
    "real": lambda x: f"{1.5 * float(x):.2f}",
    "string": lambda x: f"${x}$",
}

current_type, current_num = [input() for _ in range(2)]
print(data_types[current_type](current_num))