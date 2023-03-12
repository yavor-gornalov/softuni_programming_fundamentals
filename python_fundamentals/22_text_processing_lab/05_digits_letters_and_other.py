# https://judge.softuni.org/Contests/Practice/Index/1739#4

string = input()

letters, nums, symbols = "", "", ""

for ch in string:
    if ch.isalpha():
        letters += ch
    elif ch.isnumeric():
        nums += ch
    else:
        symbols += ch
print(nums, letters, symbols, sep="\n")
