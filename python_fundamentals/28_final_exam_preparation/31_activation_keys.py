# https://judge.softuni.org/Contests/Practice/Index/2302#0

def find_substring(substring, text):
    if substring in text:
        print(f"{text} contains {substring}")
    else:
        print("Substring not found!")
    return text


def flip_substring_to_upper(action, start, end, text):
    start_idx = int(start)
    end_idx = int(end)
    substring = text[start_idx: end_idx]
    if action == "Upper":
        text = text[:start_idx] + substring.upper() + text[end_idx:]
    elif action == "Lower":
        text = text[:start_idx] + substring.lower() + text[end_idx:]
    print(text)
    return text


def delete_slice(start, end, text):
    start_idx = int(start)
    end_idx = int(end)
    text = text[:start_idx] + text[end_idx:]
    print(text)
    return text


commands = {
    "Contains": find_substring,
    "Flip": flip_substring_to_upper,
    "Slice": delete_slice
}

activation_key = input()
while True:
    line = input()
    if line == "Generate":
        break

    command, *args = line.split(">>>")
    activation_key = commands[command](*args, activation_key)

print(f"Your activation key is: {activation_key}")
