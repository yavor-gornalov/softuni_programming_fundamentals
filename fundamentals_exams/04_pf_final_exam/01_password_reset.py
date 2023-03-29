# https://judge.softuni.org/Contests/Practice/Index/2303#0

password = input()

while True:
    command = input()
    if command == "Done":
        break
    command_args = command.split()
    action = command_args[0]
    if action == "TakeOdd":
        password = password[1:len(password):2]
    elif action == "Cut":
        index = int(command_args[1])
        length = int(command_args[2])
        password = password.replace(password[index:index + length], "", 1)
    elif action == "Substitute":
        string = command_args[1]
        substitute = command_args[2]
        if string not in password:
            print("Nothing to replace!")
            continue
        password = password.replace(string, substitute)
    print(password)
print(f"Your password is: {password}")
