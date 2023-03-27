# https://judge.softuni.org/Contests/Practice/Index/2307#0

message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    command_args = command.split(":|:")
    action = command_args[0]
    if action == "InsertSpace":
        index = int(command_args[1])
        message = message[:index] + " " + message[index:]
    elif action == "Reverse":
        substring = command_args[1]
        if substring in message:
            message = message.replace(substring, "", 1) + substring[::-1]
        else:
            print("error")
            continue
    elif action == "ChangeAll":
        substring = command_args[1]
        replacement = command_args[2]
        message = message.replace(substring, replacement)
    print(message)
print(f"You have a new text message: {message}")
