# https://judge.softuni.org/Contests/Practice/Index/1729#0


def custom_print(typ, text):
    if typ == "int":
        print(int(text) * 2)
    elif typ == "real":
        print(f"{float(text) * 1.5:.2f}")
    elif typ == "string":
        print(f"${text}$")


input_type = input()
string = input()
custom_print(typ=input_type, text=string)
