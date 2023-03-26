# https://judge.softuni.org/Contests/Practice/Index/2518#0

stops = input()

while True:
    command = input()
    if command == "Travel":
        break
    command_args = command.split(":")
    action = command_args[0]
    if action == "Add Stop":
        index = int(command_args[1])
        string = command_args[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
    elif action == "Remove Stop":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if 0 <= start_index <= end_index < len(stops):
            stops = stops.replace((stops[start_index:end_index + 1]), "")
    elif action == "Switch":
        old_string = command_args[1]
        new_string = command_args[2]
        stops = stops.replace(old_string, new_string)
    print(stops)
print(f"Ready for world tour! Planned stops: {stops}")
