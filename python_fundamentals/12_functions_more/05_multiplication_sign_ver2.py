# https://judge.softuni.org/Contests/Practice/Index/1729#4

def get_multiplications_sign(nums) -> str:
    if 0 in nums:
        return "zero"
    if len([x for x in nums if x < 0]) % 2 == 0:
        return "positive"
    return "negative"


numbers = [int(input()) for _ in range(3)]

print(get_multiplications_sign(numbers))
