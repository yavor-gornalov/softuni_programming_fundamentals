# https://judge.softuni.org/Contests/Practice/Index/1723#0

first_number, second_number = [int(input()) for _ in range(2)]

print(f"Before:\na = {first_number}\nb = {second_number}")
first_number, second_number = second_number, first_number
print(f"After:\na = {first_number}\nb = {second_number}")
