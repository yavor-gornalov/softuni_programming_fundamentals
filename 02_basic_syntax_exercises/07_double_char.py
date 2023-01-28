# https://judge.softuni.org/Contests/Compete/Index/1719#6

command = input()

while not command == "End":

    if not command == "SoftUni":
        double_command = ""
        for ch in command:
            double_command += 2 * ch
        print(double_command)

    command = input()
