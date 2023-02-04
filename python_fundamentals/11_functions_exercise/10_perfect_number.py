# https://judge.softuni.org/Contests/Compete/Index/1728#9

def perfect_number(num: int):
    divisor = 1
    sum_divisors = 0
    while divisor < num:
        if not num % divisor:
            sum_divisors += divisor
        if sum_divisors > num:
            break
        divisor += 1
    return sum_divisors == num and not num == 0


number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
