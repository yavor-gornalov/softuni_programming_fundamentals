# https://judge.softuni.org/Contests/Practice/Index/1720#0

def ord_digit(digit):
    return ord(digit)


number = list(input())

number.sort(reverse=True, key=ord_digit)
largest_number = ""
for i in number:
    largest_number += i

print(largest_number)
