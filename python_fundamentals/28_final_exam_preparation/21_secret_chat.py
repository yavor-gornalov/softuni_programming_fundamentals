# https://judge.softuni.org/Contests/Practice/Index/2307#0

def insert_space(text, idx_str):
    return text[:int(idx_str)] + " " + text[int(idx_str):]


def reverse_substring(text, substring):
    if substring not in text:
        print("error")
        return text
    return text.replace(substring, "", 1) + substring[::-1]


def change_all(text, substring, replacement):
    while substring in text:
        text = text.replace(substring, replacement)
    return text


commands = {
    "InsertSpace": insert_space,
    "Reverse": reverse_substring,
    "ChangeAll": change_all
}

encrypted_text = input()

while True:
    tokens = input()
    if tokens == "Reveal":
        print(f"You have a new text message: {encrypted_text}")
        break

    command, *args = tokens.split(":|:")
    result = commands[command](encrypted_text, *args)
    if result != encrypted_text:
        encrypted_text = result
        print(encrypted_text)
