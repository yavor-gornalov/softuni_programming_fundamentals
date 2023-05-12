# https://judge.softuni.org/Contests/Compete/Index/1719#2

messages_count = int(input())

for _ in range(messages_count):
    number_code = int(input())

    if number_code == 86:
        message = "How are you?"
    elif number_code == 88:
        message = "Hello"
    elif number_code < 88:
        message = "GREAT!"
    else:
        message = "Bye."

    print(message)
