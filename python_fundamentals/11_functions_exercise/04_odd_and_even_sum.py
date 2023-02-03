# https://judge.softuni.org/Contests/Compete/Index/1728#3

def odd_even_sum(number: str):
    odd_sum, even_sum = 0, 0
    for digit in number:
        digit = int(digit)
        if digit % 2:
            odd_sum += digit
        else:
            even_sum += digit

    return odd_sum, even_sum


num = input()
odds, evens = odd_even_sum(number=num)
print(f"Odd sum = {odds}, Even sum = {evens}")
