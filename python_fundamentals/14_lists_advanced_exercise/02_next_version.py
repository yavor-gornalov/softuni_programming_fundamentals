# https://judge.softuni.org/Contests/Compete/Index/1731#1


def version_calc(version: str):
    version_number = int(version.replace(".", ""))
    next_version_string = list(str(version_number + 1))
    return ".".join(next_version_string)


current_version = input()
print(version_calc(version=current_version))
