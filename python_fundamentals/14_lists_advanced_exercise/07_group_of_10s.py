# https://judge.softuni.org/Contests/Compete/Index/1731#6

nums = [int(x) for x in input().split(", ")]

boundary = 10
while not nums == []:
    current_nums = [num for num in nums if num <= boundary]
    nums = list(filter(lambda n: n not in current_nums, nums))
    print(f"Group of {boundary}'s: {current_nums}")
    boundary += 10
