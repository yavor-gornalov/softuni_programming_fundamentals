# https://judge.softuni.org/Contests/Practice/Index/2525#0

message = input()

while True:
    instruction = input()
    if instruction == "Decode":
        break
    instruction_args = instruction.split("|")
    operation = instruction_args[0]
    if operation == "Move":
        letters_count = int(instruction_args[1])
        message = message[letters_count:] + message[:letters_count]
    elif operation == "Insert":
        index = int(instruction_args[1])
        value = instruction_args[2]
        message = message[:index] + value + message[index:]
    elif operation == "ChangeAll":
        substring = instruction_args[1]
        replacement = instruction_args[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
