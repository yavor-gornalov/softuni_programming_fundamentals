# https://judge.softuni.org/Contests/Practice/Index/2302#0

key = input()

while True:
    command = input()
    if command == "Generate":
        break
    command_args = command.split(">>>")
    action = command_args[0]
    if action == "Contains":
        substring = command_args[1]
        if substring not in key:
            print("Substring not found!")
        else:
            print(f"{key} contains {substring}")
    elif action == "Flip":
        to_upper = command_args[1] == "Upper"
        start_index = int(command_args[2])
        end_index = int(command_args[3])
        if to_upper:
            key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
        else:
            key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
        print(key)
    elif action == "Slice":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        key = key.replace(key[start_index:end_index], "")
        print(key)

print(f"Your activation key is: {key}")
