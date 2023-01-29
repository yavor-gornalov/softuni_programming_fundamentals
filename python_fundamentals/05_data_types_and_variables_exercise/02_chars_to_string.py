# https://judge.softuni.org/Contests/Compete/Index/1722#1

def chars_to_str():
    result = ""
    for _ in range(3):
        string = input()
        result += string
    return result


# main
new_string = chars_to_str()
print(new_string)
