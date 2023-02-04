# https://judge.softuni.org/Contests/Compete/Index/1728#8

def password_validator(password: str):
    is_valid = True
    num_count = sum(ch.isdigit() for ch in password)
    letter_count = sum(ch.isalpha() for ch in password)
    if len(password) not in range(6, 11):
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if num_count + letter_count < len(password):
        is_valid = False
        print("Password must consist only of letters and digits")
    if num_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


user_pass = input()
password_validator(user_pass)
