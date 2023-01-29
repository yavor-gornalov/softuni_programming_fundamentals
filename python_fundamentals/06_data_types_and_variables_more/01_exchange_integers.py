# https://judge.softuni.org/Contests/Practice/Index/1723#0

a = int(input())
b = int(input())

print(f"Before:\na = {a}\nb = {b}")
c = a
a = b
b = c
print(f"After:\na = {a}\nb = {b}")
