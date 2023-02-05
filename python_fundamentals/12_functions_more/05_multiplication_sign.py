# https://judge.softuni.org/Contests/Practice/Index/1729#4

def multiplication_sign(a, b, c):
    nums = [a, b, c]
    if 0 in nums:
        print("zero")
    else:
        count_negatives = len([n for n in nums if n < 0])
        if count_negatives % 2:
            print("negative")
        else:
            print("positive")


first_num = int(input())
second_num = int(input())
third_num = int(input())
multiplication_sign(first_num, second_num, third_num)
