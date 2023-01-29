# https://judge.softuni.org/Contests/Compete/Index/1719#2

def chat_codes(code):
    if code == 88:
        text = "Hello"
    elif code == 86:
        text = "How are you?"
    elif code < 88:
        text = "GREAT!"
    else:
        text = "Bye."
    return text


# main
n = int(input())

for _ in range(n):
    message = int(input())
    result = chat_codes(message)
    print(result)
