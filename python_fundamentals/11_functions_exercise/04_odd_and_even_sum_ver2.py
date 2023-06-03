# https://judge.softuni.org/Contests/Compete/Index/1728#3

def print_odd_even_sum(number):
    evens, odds = [], []
    for digit in number:
        if int(digit) % 2 == 0:
            evens.append(int(digit))
        else:
            odds.append(int(digit))
    print(f"Odd sum = {sum(odds)}, Even sum = {sum(evens)}")


num = input()
print_odd_even_sum(num)
