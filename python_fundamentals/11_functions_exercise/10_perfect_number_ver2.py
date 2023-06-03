# https://judge.softuni.org/Contests/Compete/Index/1728#9

def perfect_number(num):
    divisors = [i for i in range(1, num // 2 + 1) if num % i == 0]
    return sum(divisors) == num and num != 0


number = int(input())
print("We have a perfect number!") if perfect_number(number) else print("It's not so perfect.")
