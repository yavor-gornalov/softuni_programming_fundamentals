# https://judge.softuni.org/Contests/Compete/Index/1722#0

first_int = int(input())
second_int = int(input())
third_int = int(input())
fourth_int = int(input())

result = 0
result += first_int + second_int
result //= third_int
result *= fourth_int

print(result)
