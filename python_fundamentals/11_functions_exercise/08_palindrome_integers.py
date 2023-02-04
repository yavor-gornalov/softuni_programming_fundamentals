# https://judge.softuni.org/Contests/Compete/Index/1728#7

def palindrome(number): return number[::-1] == number


nums = [n for n in input().split(", ")]

for num in nums:
    print(palindrome(num))
